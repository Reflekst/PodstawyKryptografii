from math import ceil
from Crypto.Cipher import AES
import MessagePreprocessing
import blokCipher as bc

def ecbEncrypt(self):  # szyfrowanie ECB
    if len(self.textToEncrypt) == 0:
        return "Nie podano wiadomości do szyfrowania!"
    cipher = AES.new(self.cipherKey, AES.MODE_ECB)
    self.cipherArray = []
    byteBlocks = list(
        MessagePreprocessing.split(self.textToEncrypt, ceil(len(self.textToEncrypt) / 16)))  # dzielę wszystkie bajty na bloki o długości 16
    for block in byteBlocks:
        tempArray = []
        for i in cipher.encrypt(block):  # każdy blok szyfruje gotową biblioteką dla ECB
            tempArray.append(i)
        self.cipherArray.append(tempArray)  # tworzę szyfrogram - lista podlist o długości bloku
    print(self.cipherArray)
    string = ""



def ecbDecrypt(self):  # deszfrowanie ECB
    decipher = AES.new(self.cipherKey, AES.MODE_ECB)
    decryptedArray = []
    cryptedArray = []
    for block in self.cipherArray:  # dla każdego bloku wykonuje deszyfrowanie
        diffrence = 16 - len(block)
        while len(block) != 16:
            block.append(diffrence)
        for i in decipher.decrypt(bytes(block)):
            decryptedArray.append(i)  # zapisuje bajty po deszyfrowaniu
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
    for x in decryptedArray:  # ponownie generuje tekst jawny z bajtów
        string += chr(x)
    if len(MessagePreprocessing.unpad(string)) < 16:
        print(string)
        print()
    else:
        print()
        print(MessagePreprocessing.unpad(string))  # zwracam oryginalny tekst