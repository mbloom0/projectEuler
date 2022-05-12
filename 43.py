#Problem 43: Sub-string divisibility
""" The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property. """
from itertools import permutations
from sympy import factorint, isprime
import time

def pandigital(n):
    n=str(n)
    """Returns if a number (int) n is 0 thru 9 pandigital"""
    pandigEq = ''.join(list(map(str,list(range(0,10)))))
    if len(n) != len(pandigEq):
        return False
    n=list(map(int,n))
    n.sort()
    n = ''.join(map(str,n))
    pandigEq=list(map(int,pandigEq))
    pandigEq.sort()
    pandigEq = ''.join(map(str,pandigEq))
    for i in range(len(n)):
        if n[i] != pandigEq[i]:
            return False
    return True

firstPrimes = list(filter(isprime,range(2,24)))
def subStrDivProp(n):#NOTE: feed this pandigital integers
    #takes a 10 digit number and checks if the first 7 primes (2-17) are factors of the seven substrings chars 2-4,3-5,...8-10. (starting at first digit =1)
    substrs = [str(n)[i:i+3] for i in range(1,7+1)]
    if all(factorLists.__contains__(y) for (factorLists, y) in zip([factorint(int(x)).keys() for x in substrs], firstPrimes[0:len(substrs)])):
        return True
    return False

f = open("zeroToNinePandigitals.txt",'r')
if f.readlines() == []:
    print("empty file! calculating and writing pandigitals to file...")
    startt = time.time()
    f.close()
    with open("zeroToNinePandigitals.txt",'w') as f:
        f.writelines(list(map(lambda x: str(x)+"\n",filter((lambda x: True if len(x)==10 else False), [''.join(x) for x in set(permutations("0123456789")) if pandigital(int(''.join(x)))]))))
    print("Took: not writable(seconds) ", time.time()-startt)


with open("zeroToNinePandigitals.txt") as f:
    print("reading file!")
    zeroToNinePandigitals = map(int,[x.strip('\n') for x in f.readlines()])
startt = time.time()
l = list(filter(subStrDivProp,zeroToNinePandigitals))
print(l)
ans = sum(l)
print(ans)
print("Took: not writable(seconds) ", time.time()-startt)