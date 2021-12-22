from textwrap import wrap
import BBS as gen

def getBinaryText(self,text):
    binaryString =""
    for char in text:
        binaryString = binaryString +  str(bin(ord(char))[2:]).zfill(7) #przerabianie string na binary string
    return binaryString

def getBinaryString(self,length):
    return gen.BlumBlumShub().bits(length)

class streamEncoder(object):
    """description of class"""
    def __init__(self,text = "", path =""):
        if path == "":
            self.clearText = text
        else:
            with open(path) as f:
                  self.clearText = f.read()
                  f.close()
        self.message =  getBinaryText(self,self.clearText) #jawny binarny
        self.bbs = ""
        self.endcoder = ""


    def setBBS(self): #ustaw klucz - bbs
        self.bbs = getBinaryString(self,len(self.message))  #pobieramy długość ciągu bitów tekstu i generatorem BBS tworzymy ciąg bitów o tej samej długości
                                                                                                                                      
    def setEncoder(self): #ustaw szyfrogram
        cryptogram =""
        for i in range(0,len(self.message)):
            cryptogram += str(int(self.bbs[i]) ^ int(self.message[i]))
        self.endcoder = cryptogram #

    def decrypt(self):
        plainBin=""
        for i in range(0,len(self.endcoder)): #deszyfrowanie XOR wykonywany na szyfrogamie i kluczu
            plainBin += str(int(self.endcoder[i]) ^ int(self.bbs[i]))
        plainTxt = ""
        for asci in wrap(plainBin,7):
            plainTxt+= chr(int(asci,2))
        print(plainTxt)
        return plainTxt # zwróć text jawny


        

