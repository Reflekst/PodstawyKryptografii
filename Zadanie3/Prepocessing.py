import random
from math import gcd as bltin_gcd #greatest common divisor
from textwrap import wrap

def GreatestCommonDivisor(a, n):
    return bltin_gcd(a, n) == 1 #NWD

def Split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def GeneratePrimeNumber():
    min_val = 1001
    max_val = 10000
    temp_rand = random.randint(min_val,max_val)
    while temp_rand is not isPrime(temp_rand):
        temp_rand = random.randint(min_val,max_val)
    return temp_rand

def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    
    return True

#def GeneratePrimeNumber(lower = 1000, upper = 9999):
#    primeNumberArray = []
#    for num in range(lower,upper + 1):  
#        if num > 1:  
#            for i in range(2,num):  
#                if (num % i) == 0:  
#                    break  
#        else:
#            primeNumberArray.append(num)
#    return primeNumberArray

#def GetPrimeNumber(primeNumberArray):
#    random.choice(primeNumberArray)             