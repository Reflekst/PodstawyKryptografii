from typing import Text
import ECB as ecb
import CBC as cbc
import CBCC as cbcc
import blokCipher as bc
import time

primaryMessage = "Nie dosc, ze nie moge bialego pieczywa, to jeszcze musialem odstawic moj ulubiony napoj - syrop z cebuli na cukrze!"
#Nie dosc, ze nie moge bialego pieczywa, to jeszcze musialem odstawic moj ulubiony napoj - syrop z cebuli na cukrze!"


def start():

    keyToDecrypt = "B23R88Das59593lK"


    message = primaryMessage

    #f = open("100KB.txt")

    #message = f.read().replace("\n","")

    #f.close()

    #print(len(message))
    #print(message)

    print("Wynik szyfrowania i deszyfrowania trybem ECB:")
    print()
    blockA = bc.blockCipher(text = message, key = keyToDecrypt, IV = "")
    start_time = time.monotonic()
    print("ECB szyfrowanie: ")
    print()
    ecb.ecbEncrypt(blockA)
    blockA.cipherArray.remove(blockA.cipherArray[1])
    print()
    print('seconds: ', time.monotonic() - start_time)
    start_time = time.monotonic()
    print()

    print("ECB deszyfrowanie: ")
    print()
    ecb.ecbDecrypt(blockA)
    print('seconds: ', time.monotonic() - start_time)
    
    print("Wynik szyfrowania i deszyfrowania trybem CBC:")
    blockB = bc.blockCipher(text = message, key = keyToDecrypt, IV = "")
    start_time = time.monotonic()
    cbc.cbcEncrypt(blockB)
    print()
    print("CBC szyfrowanie:")
    print('seconds: ', time.monotonic() - start_time)
    blockB.cipherArray.remove(blockB.cipherArray[1])
    print()
    start_time = time.monotonic()
    print("CBC deszyfrowanie: ")
    print()
    cbc.cbcDecrypt(blockB)
    print()
    print('seconds: ', time.monotonic() - start_time)

    print("Wynik szyfrowania i deszyfrowania trybem CBCC:")
    blockC = bc.blockCipher(text = message, key = keyToDecrypt, IV = "")
    start_time = time.monotonic()
    cbcc.cbccEncrypt(blockC)
    print()
    print("CBCC szyfrowanie: ")
    print()
    print('seconds: ', time.monotonic() - start_time)
    print()
    blockC.cipherArray.remove(blockC.cipherArray[1])
    start_time = time.monotonic()
    print()
    print("CBCC deszyfrowanie: ")
    print()
    cbcc.cbccDecrypt(blockC)
    print()
    print('seconds: ', time.monotonic() - start_time)
    print()


    print("Powielić wybrany blok")
    print("Wynik szyfrowania i deszyfrowania trybem ECB:")
    blockA = bc.blockCipher(text =message, key = keyToDecrypt)
    ecb.ecbEncrypt(blockA)
    blockA.cipherArray.insert(2,blockA.cipherArray[1])
    ecb.ecbDecrypt(blockA)
    print()

    print("Wynik szyfrowania i deszyfrowania trybem CBC:")
    blockB = bc.blockCipher(text =message, key = keyToDecrypt)
    cbc.cbcEncrypt(blockB)
    blockB.cipherArray.insert(2,blockB.cipherArray[1])
    cbc.cbcDecrypt(blockB)
    print()

    print("Wynik szyfrowania i deszyfrowania trybem CBCC:")
    blockC = bc.blockCipher(text =message, key = keyToDecrypt)
    cbcc.cbccEncrypt(blockC)
    blockC.cipherArray.insert(2,blockC.cipherArray[1])
    cbcc.cbccDecrypt(blockC)
    print()

    print("Zamienić bloki miejscami ")
    print("Wynik szyfrowania i deszyfrowania trybem ECB:")
    blockA = bc.blockCipher(text =message, key = keyToDecrypt)
    ecb.ecbEncrypt(blockA)
    temp1 = blockA.cipherArray[2]
    temp2 = blockA.cipherArray[3]
    blockA.cipherArray[2] = temp2
    blockA.cipherArray[3] = temp1
    ecb.ecbDecrypt(blockA)
    print()

    print("Wynik szyfrowania i deszyfrowania trybem CBC:")
    blockB = bc.blockCipher(text =message, key = keyToDecrypt)
    cbc.cbcEncrypt(blockB)
    temp1 = blockB.cipherArray[2]
    temp2 = blockB.cipherArray[3]
    blockB.cipherArray[2] = temp2
    blockB.cipherArray[3] = temp1
    cbc.cbcDecrypt(blockB)
    print()

    print("Wynik szyfrowania i deszyfrowania trybem CBCC:")
    blockC = bc.blockCipher(text =message, key = keyToDecrypt)
    cbcc.cbccEncrypt(blockC)
    temp1 = blockC.cipherArray[2]
    temp2 = blockC.cipherArray[3]
    blockC.cipherArray[2] = temp2
    blockC.cipherArray[3] = temp1
    cbcc.cbccDecrypt(blockC)
    print()

    print("Wiadomość do szyfrowania:")
    print(message)
    print()


    print("Zmiana wartości bajtu")
    print("Wynik szyfrowania i deszyfrowania trybem ECB:")
    blockA = bc.blockCipher(text =message, key = keyToDecrypt)
    ecb.ecbEncrypt(blockA)
    blockA.cipherArray[2][5] = blockA.cipherArray[2][5] +1
    ecb.ecbDecrypt(blockA)
    print()

    print("Wynik szyfrowania i deszyfrowania trybem CBC:")
    blockB = bc.blockCipher(text =message, key = keyToDecrypt)
    cbc.cbcEncrypt(blockB)
    blockB.cipherArray[2][5] = blockA.cipherArray[2][5] +1

    cbc.cbcDecrypt(blockB)
    print()

    print("Wynik szyfrowania i deszyfrowania trybem CBCC:")
    blockC = bc.blockCipher(text =message, key = keyToDecrypt)
    cbcc.cbccEncrypt(blockC)
    blockC.cipherArray[2][5] = blockA.cipherArray[2][5] +1

    cbcc.cbccDecrypt(blockC)
    print()

    print("Wiadomość do szyfrowania:")
    print(message)
    print()

    print("Zamienić wewnątrz bloku bajty miejscami ")
    print("Wynik szyfrowania i deszyfrowania trybem ECB:")
    blockA = bc.blockCipher(text =message, key = keyToDecrypt)
    ecb.ecbEncrypt(blockA)
    temp1 = blockA.cipherArray[2][9]
    temp2 = blockA.cipherArray[2][10]
    blockA.cipherArray[2][9] = temp2
    blockA.cipherArray[2][10] = temp1
    ecb.ecbDecrypt(blockA)
    print()

    print("Wynik szyfrowania i deszyfrowania trybem CBC:")
    blockB = bc.blockCipher(text =message, key = keyToDecrypt)
    cbc.cbcEncrypt(blockB)
    temp1 = blockB.cipherArray[2][9]
    temp2 = blockB.cipherArray[2][10]
    blockB.cipherArray[2][9] = temp2
    blockB.cipherArray[2][10] = temp1

    cbc.cbcDecrypt(blockB)
    print()

    print("Wynik szyfrowania i deszyfrowania trybem CBCC:")
    blockC = bc.blockCipher(text =message, key = keyToDecrypt)
    cbcc.cbccEncrypt(blockC)
    temp1 = blockC.cipherArray[2][9]
    temp2 = blockC.cipherArray[2][10]
    blockC.cipherArray[2][9] = temp2
    blockC.cipherArray[2][10] = temp1
    cbcc.cbccDecrypt(blockC)
    print()

    print("Wiadomość do szyfrowania:")
    print(message)
    print()

    print("Usunąć fragment bloku")
    print("Wynik szyfrowania i deszyfrowania trybem ECB:")
    blockA = bc.blockCipher(text =message, key = keyToDecrypt)
    ecb.ecbEncrypt(blockA)
    blockA.cipherArray[2].remove(blockA.cipherArray[2][12])
    ecb.ecbDecrypt(blockA)
    print()

    print("Wynik szyfrowania i deszyfrowania trybem CBC:")
    blockB = bc.blockCipher(text =message, key = keyToDecrypt)
    cbc.cbcEncrypt(blockB)
    blockB.cipherArray[2].remove(blockB.cipherArray[2][12])
    cbc.cbcDecrypt(blockB)
    print()


    print("Wynik szyfrowania i deszyfrowania trybem CBCC:")
    blockC = bc.blockCipher(text =message, key = keyToDecrypt)
    cbcc.cbccEncrypt(blockC)
    blockC.cipherArray[2].remove(blockC.cipherArray[2][12])

    cbcc.cbccDecrypt(blockC)
    print()

start()