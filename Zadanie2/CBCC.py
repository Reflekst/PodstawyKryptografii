from math import ceil
from Crypto.Cipher import AES
import MessagePreprocessing

def cbccEncrypt(self):
    if len(self.textToEncrypt) == 0:
        return "Nie podano wiadomości do szyfrowania!"
    if self.IV == "" or len(self.IV) != 128:  # blok 128 bitów
        self.IV = MessagePreprocessing.generateIV() # losowe generowanie IV
    byteBlocks = list(
        MessagePreprocessing.split(self.textToEncrypt, ceil(len(self.textToEncrypt) / 16)))  # jak w ECB dzielę na podlisty(bloki)
    currentIV = self.IV
    controllSum = MessagePreprocessing.getBits(byteBlocks[0])
    self.cipherArray = []
    cipher = AES.new(self.cipherKey, AES.MODE_ECB)

    for idx, byteBlock in enumerate(byteBlocks):
        if byteBlock != byteBlocks[-1]: 
            controllSum = MessagePreprocessing.xorOperation(MessagePreprocessing.getBits(byteBlock), controllSum) # tworzenie sumy kontrolnej
        #print(str(idx)+" "+controllSum)
        if byteBlock == byteBlocks[-1]:
            topreEncrypt = MessagePreprocessing.xorOperation(MessagePreprocessing.getBits(byteBlock), controllSum) # XOR sumy kontrolnej z ostatnim blokiem
            toEncrypt = MessagePreprocessing.xorOperation(topreEncrypt,currentIV)  # wykonuję operację XOR na bloku waidomiści jawnej i IV
        else:
            toEncrypt = MessagePreprocessing.xorOperation(MessagePreprocessing.getBits(byteBlock),currentIV)
        tempIV = ""
        tempArray = []
        for enc in cipher.encrypt(bytes(MessagePreprocessing.getBytes(toEncrypt))):  # szyfruje blok za pomocą gotowej implementacji ECB
            tempArray.append(enc)
            tempIV += str(bin(enc)[2:]).zfill(8)  # tworzę zaszyfrowany blok i generuje bity, które będą użyte do następnej operacji XOR z blokiem tesktu
        self.cipherArray.append(tempArray)
        currentIV = tempIV
    print()
    #print(self.cipherArray)
    print()

def cbccDecrypt(self):
    currentIV = self.IV
    decryptedArray = []
    decryptedTempArray = []
    cryptedArray = []
    controllSum = ""
    decipher = AES.new(self.cipherKey, AES.MODE_ECB)
    for idx, block in enumerate(self.cipherArray):  # dla bloków 16 bajtowych z szyfrogramu
        diffrence = 16 - len(block)  # jeżeli blok jest za mały, dokonuję dopełnienia
        while len(block) != 16:
            block.append(diffrence)
        tempOutIV = ""
        tempSum = ""
        for enc in decipher.decrypt(bytes(block)):  # deszyfruje blok szyfrogramu
            tempOutIV += str(bin(enc)[2:]).zfill(8)

        for i in MessagePreprocessing.getBytes(MessagePreprocessing.xorOperation(tempOutIV, currentIV)):  # wykonuję operację XOR z aktualnym IV
            if block == self.cipherArray[-1]:
                decryptedTempArray.append(i)
            else:    
                decryptedArray.append(i)
                tempSum += str(bin(i)[2:]).zfill(8)

        if block == self.cipherArray[0]:
            controllSum = MessagePreprocessing.xorOperation(tempSum, tempSum)

        if block != self.cipherArray[-1] and block != self.cipherArray[0]:
            controllSum = MessagePreprocessing.xorOperation(tempSum, controllSum)

        #print(str(idx)+" "+controllSum)

        if block == self.cipherArray[-1]:
            #print(block)
            for i in MessagePreprocessing.getBytes(MessagePreprocessing.xorOperation(MessagePreprocessing.getBits(decryptedTempArray), controllSum)):
                decryptedArray.append(i)
        
        for i in block:
            cryptedArray.append(i) 

        currentIV = ""
        for i in block:
            currentIV += str(bin(i)[2:]).zfill(8)  # w kolejnej operacji do funkcji XOR wykorzystuje się poprzedni blok szyfrogramu

    #string = ""
    #for x in cryptedArray:  # ponownie generuje tekst jawny z bajtów
    #    string += chr(x)
    #if len(MessagePreprocessing.unpad(string)) < 16:
    #    print(string)
    #    print()
    #else:
    #    print()
    #    print(MessagePreprocessing.unpad(string))  # zwracam oryginalny tekst

    string = ""
    for x in decryptedArray:  # przywracam oryginalny tekst
        string += chr(x)

    if len(MessagePreprocessing.unpad(string)) < 16:
        print(string)
        print()
    else:
        print(MessagePreprocessing.unpad(string))
        print()