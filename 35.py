#Problem 35: Circular primes
""" 
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
from sympy import isprime

def genRotations(n):
    rotations = []
    n = str(n)
    newN = n
    for i in range(len(n)):
        newN =  newN[1:] + newN[0]
        rotations.append(int(newN))
    return rotations

def circularPrime(n):
    if all(map(isprime, genRotations(n))):
        return True
    return False

circPrimeUnderMil = [x for x in range(10**6) if circularPrime(x)]
""" 
spRange = list(range(10**6))
for x in spRange:
    if circularPrime(x):
        print(genRotations(x))
        for y in list(set(genRotations(x))):
            spRange.remove(y)
        circPrimeUnderMil.append(x)
 """
print(circPrimeUnderMil)
print(len(circPrimeUnderMil))
""" 
uniqueCircPrimes = []
temp = {}
for circ in circPrimeUnderMil:
    rots = genRotations(circ)
    rotInUni = False
    for x in rots:
        if temp.keys().__contains__(x):
            temp[x] +=1
            rotInUni = True
            break
    if not rotInUni:
        temp[circ] == 1 
        
print(uniqueCircPrimes)

print(genRotations(123))
 """
