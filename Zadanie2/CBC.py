from math import ceil
from Crypto.Cipher import AES
import MessagePreprocessing

def cbcEncrypt(self):
    if len(self.textToEncrypt) == 0:
        return "Nie podano wiadomości do szyfrowania!"
    if self.IV == "" or len(self.IV) != 128:  # blok 128 bitów
        self.IV = MessagePreprocessing.generateIV() # losowe generowanie IV
        currentIV = self.IV
    else:
        currentIV = self.IV  
    byteBlocks = list(
        MessagePreprocessing.split(self.textToEncrypt, ceil(len(self.textToEncrypt) / 16)))  # jak w ECB dzielę na podlisty(bloki)

    self.cipherArray = []
    cipher = AES.new(self.cipherKey, AES.MODE_ECB)

    for byteBlock in byteBlocks:
        toEncrypt = MessagePreprocessing.xorOperation(MessagePreprocessing.getBits(byteBlock),currentIV)  # wykonuję operację XOR na bloku waidomiści jawnej i IV
        tempIV = ""
        tempArray = []
        for enc in cipher.encrypt(bytes(MessagePreprocessing.getBytes(toEncrypt))):  # szyfruje blok za pomocą gotowej implementacji ECB
            tempArray.append(enc)
            tempIV += str(bin(enc)[2:]).zfill(8)  # tworzę zaszyfrowany blok i generuje bity, które będą użyte do następnej operacji XOR z blokiem tesktu
        self.cipherArray.append(tempArray)
        currentIV = tempIV
    #print(self.cipherArray)

def cbcDecrypt(self):
    currentIV = self.IV
    decryptedArray = []
    cryptedArray = []
    decipher = AES.new(self.cipherKey, AES.MODE_ECB)

    for block in self.cipherArray:  # dla bloków 16 bajtowych z szyfrogramu
        diffrence = 16 - len(block)  # jeżeli blok jest za mały, dokonuję dopełnienia
        while len(block) != 16:
            block.append(diffrence)
        tempOut = ""
        for enc in decipher.decrypt(bytes(block)):  # deszyfruje blok szyfrogramu
            tempOut += str(bin(enc)[2:]).zfill(8)

        for i in MessagePreprocessing.getBytes(MessagePreprocessing.xorOperation(tempOut, currentIV)):  # wykonuję operację XOR z aktualnym IV
            decryptedArray.append(i)

        currentIV = ""
        for i in block:
            currentIV += str(bin(i)[2:]).zfill(8)  # w kolejnej operacji do funkcji XOR wykorzystuje się poprzedni blok szyfrogramu

        for i in block:
            cryptedArray.append(i) 

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