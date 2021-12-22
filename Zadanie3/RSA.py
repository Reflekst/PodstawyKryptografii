import random
from textwrap import wrap
import Prepocessing as prep

class RSA(object):
    def __init__(self, p = 0, q = 0, e = 0, d = 0):
        if p == 0 or q == 0 or (p > 9999 or p < 1000 or q > 9999 or q < 1000 or not prep.isPrime(p) or not prep.isPrime(q)):
            p = 0
            q = 0 
            while p == q:
                p = prep.GeneratePrimeNumber()
                q = prep.GeneratePrimeNumber()                     
        self.p = p
        self.q = q
        self.c =[]
        self.n = self.p * self.q
        self.phi_n = (self.p-1) * (self.q-1)

        if e == 0 or e is not prep.isPrime(e) and not prep.GreatestCommonDivisor(e,self.phi_n):
            temp_e = random.randint(3,self.phi_n-1)
            while not prep.isPrime(temp_e) and not prep.GreatestCommonDivisor(temp_e,self.phi_n):
                  temp_e = random.randint(3,self.phi_n-1)
            self.e = temp_e
        else:
            self.e = e
        if d ==0:
            temp_d = 3
            while (self.e* temp_d) % self.phi_n !=1 and temp_d < self.phi_n:
                  temp_d = temp_d +1
            if temp_d>=self.phi_n:
                print("Błędne dane")
            self.d = temp_d
        else:
            self.d = d

    def encryptMessage(self,message,e,n):
            naturalMess = ""
            for byte in str.encode(message):
                i = int(byte)
                if i<100:
                    i = i+300
                naturalMess += str(i)
            toEncrypt = wrap(naturalMess,6)

            self.c =[]
            for m in toEncrypt:
                self.c.append(int(m)**e % n)
            toPrint =""
            for x in self.c:
                toPrint+= str(x) +" "
            print(toPrint)

    def decryptMessage(self,message,d,n):
            offset = 300
            mD = []
            for cs in message:
                val = cs ** d % n
                values = wrap(str(val),3)
                for value in values:
                    val = int(value)
                    if val >=offset:
                        val = val -offset
                    mD.append(val)
                    print(chr(val),end="")
            print()
        

