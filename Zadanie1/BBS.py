import random
from math import gcd as bltin_gcd

def GreatestCommonDivisor(a, n):
    return bltin_gcd(a, n) == 1 #NWD
 
def BlumNumber(p,q):
    if p ==0 or q ==0:
        return 246947 * 246971 #Liczby pierwsze przystajace modulo do 4 = 3
    return p*q

def RandomNaturalNumber(self):
    a = random.randint(2, self.n - 1)   #Generujemy liczbę naturalną w przedziale do liczby Bluma -1
    return a

class BlumBlumShub(object):
    def __init__(self, a = None, p = 0, q = 0):
        self.n = BlumNumber(p,q)  # obliczamy liczbę Bluma
        if a is None: # jeżeli a jest nullem generujemy losowa liczbe naturalna i sprawdzamy czy NWD z Bluma == 1
            self.a = RandomNaturalNumber(self)
            while not GreatestCommonDivisor(self.a, self.n):
                self.a = RandomNaturalNumber(self)
        else: self.a == a
        self.a = (self.a**2) % self.n #x0 = a^2 mod n

    def singlebit(self):
        while True:
            yield self.a % 2  #modulo 2 w celu uzskania najmłodszego bitu
            self.a = pow(self.a, 2, self.n ) #podnosimy x do kwadratu i robimy modulo z liczbą bluma

    def bits(self, r=20): #funkcja zwraca nam ciąg binarny o długości r
        bitsStream = ''
        print(self.singlebit)
        for bit in self.singlebit():
            bitsStream += str(bit)
            if len(bitsStream) == r:
                break
 
        return bitsStream #Wygenerowany ciąg o długości r