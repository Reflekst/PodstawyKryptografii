from math import e
import RSA as RSA
import Prepocessing as prep


def printRsaKeys(rsa):
    print("Klucz publiczy: "+ str(rsa.e) +" , "+ str(rsa.n))
    print("Klucz prywatny: "+ str(rsa.d) +" , "+ str(rsa.n))

def start():

    print(prep.isPrime(1019))
    print("Zadanie 1")
    print()
    rsa = RSA.RSA(p = 1013, q = 1019)
    printRsaKeys(rsa)
    print()
    message = "Najpierw dowiedzialem sie ze jestem uczulony na cy"
    print("Wiadomość pierwotna")
    print(message)
    print()
    print("Wiadomość zaszyfrowana")
    rsa.encryptMessage(message,rsa.e,rsa.n)
    print()
    print("Wiadomość odszyfrowana")
    rsa.decryptMessage(rsa.c,rsa.d,rsa.n)
    print()


    print("Zadanie 2")
    print()
    rsaA = RSA.RSA(p = 1013, q = 1019)
    rsaB = RSA.RSA(p = 1033, q = 1049)
    print("Para kluczy pierwszej osoby")
    printRsaKeys(rsaA)
    print()
    print("Para kluczy drugiej osoby")
    printRsaKeys(rsaB)
    print()
    message = "Dokument do podpisu"
    print("Pierwsza osoba")
    print()
    print("Dokument przed podpisaniem")
    print(message)
    print()
    print("Zaszyfrowany")
    rsaA.encryptMessage(message,rsaA.d,rsaA.n)
    print()
    print()
    rsaA.decryptMessage(rsaA.c, rsaA.e, rsaA.n)
    print()
    print("Druga osoba")
    print()
    print("Dokument przed podpisaniem")
    print(message)
    print()
    print("Zasztfrowany")
    rsaA.encryptMessage(message,rsaB.d,rsaB.n)
    print()
    print()
    rsaA.decryptMessage(rsaB.c, rsaB.e, rsaB.n)
    

start()