import MessagePreprocessing as messpro

class blockCipher(object):
    def __init__(self, text="", key="", IV=""):
        self.cipherKey = 'BrUdaPuts4sK3ksy'  # przypisanie klucza domyślnego
        if key != "":  #jezeli nie chcemy uzyc domyslnego, czyli uzytkownik podal klucz przy tworzeniu obiektu
            tempKey = str.encode(key)
            if len(tempKey) != 16:
                print("Klucz nie składa się z 16 bajtów !! Użyto domyślnego")
            else:
                self.cipherKey = tempKey
        if len(text) == 0:
            print("Nie podano wiadomości do szyfrowania!!")
        else:
            self.textToEncrypt = messpro.prepareText(text)  # przygotowanie tekstu do szyfrowania - dopełnienie i zmiana na bajty
        self.cipherText = ""
        self.IV = IV
    
    def getPlainBits(self):
        for i in self.textToEncrypt:
            print(str(bin(i)[2:]).zfill(8) + " ", end="")
        print()

    def getPlainHEX(self):
        for i in self.textToEncrypt:
            print(str(hex(i)).lstrip("0x").zfill(2) + " ", end="")
        print()