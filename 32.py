#Problem 32: Pandigital products
""" We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
from sympy import divisors
from itertools import combinations


def pandigital(n):
    for x in n:
        if not (x in "123456789" and n.count(x) == 1 and len(n) == len("123456789")):
            return False    
    return True

panDigProducts = {}
for i in range(10000):
    for c in combinations(divisors(i),2):
        if pandigital(str(c[0])+str(c[1])+str(i)) and (c[0]*c[1] == i):
            print(str(c[0])+str(c[1])+str(i))
            panDigProducts[str(i)] = str(c[0])+"*"+str(c[1])

print(panDigProducts)    
print(str(sum(map(int,panDigProducts.keys()))))