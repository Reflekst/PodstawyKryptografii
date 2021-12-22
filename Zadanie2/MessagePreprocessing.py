import random
from textwrap import wrap

def pad(m): # dopełnienie tekstu do 128 bitowych bloków
    return m+chr(16-len(m)%16)*(16-len(m)%16)

def unpad(ct): # powrót do wiadomości pierwotnej
    return ct[:-ord(ct[-1])]

def prepareText(text):
    paddedText = pad(text)
    return str.encode(paddedText) # zwrócenie tekstu w blokach 16 bajtowych

def getBits(bytes):
    outPut =""
    for b in bytes:
        outPut+= str(bin(b)[2:]).zfill(8)
    return outPut

def getBytes(bits):
    blocks = wrap(bits,8)
    bytes = []
    for block in blocks:
        bytes.append(int(block,2))
    return bytes

def xorOperation(firstBits, secondBits):
    outPutBits = ""
    for i in range(0, len(firstBits)):
        outPutBits += str(int(firstBits[i]) ^ int(secondBits[i]))
    return outPutBits

def doXorOperation(currentIV, input, inputBin=""):
    if inputBin == "":
        for i in str.encode(input):
            inputBin += str(bin(i)[2:]).zfill(8)

    if len(inputBin) != len(currentIV):
        print("Błąd w funkcji doXorOperation")
        return

    outPutBits = ""
    for i in range(0, len(inputBin)):
        outPutBits += str(int(inputBin[i]) ^ int(currentIV[i]))

    bitsWrap = wrap(outPutBits, 8)
    outPutBytes = []
    for bits in bitsWrap:
        outPutBytes.append(int(bits, 2))
    return bytes(outPutBytes)

def generateIV():  # generowanie bloku o długości 16 z losowymi bajtami
    tempIV = []
    for x in range(0, 16):
        tempIV.append(random.randint(0, 255))
    cfbIV = []
    currentCfbIV = []
    IV = ""
    currentIV = ""
    for i in tempIV:
        cfbIV.append(i)
        currentCfbIV.append(i)
        IV += str(bin(i)[2:]).zfill(8)
        currentIV += str(bin(i)[2:]).zfill(8)
    return currentIV  

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

def getPlainBits(textToEncrypt):
    for i in textToEncrypt:
        print(str(bin(i)[2:]).zfill(8) + " ", end="")
    print()

def getPlainHEX(textToEncrypt):
    for i in textToEncrypt:
        print(str(hex(i)).lstrip("0x").zfill(2) + " ", end="")
    print()