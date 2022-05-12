#Problem 37: Truncatable primes
""" The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes. """
from math import trunc
from sympy import isprime

def truncateLeft(n):
    n = str(n)
    forms = []
    for i in range(len(n)-1):
        n = n[1:len(n)]
        forms.append(int(n))
    return forms

def truncateRight(n):
    n = str(n)
    forms = []
    for i in range(len(n)-1):
        n = n[0:len(n)-1]
        forms.append(int(n))
    return forms

truncPrimes = []
for i in range(8, 10**6):
    if isprime(i):
        if all(map(isprime,truncateLeft(i)+truncateRight(i))):
            truncPrimes.append(i)

print(truncPrimes)
print(sum(truncPrimes))