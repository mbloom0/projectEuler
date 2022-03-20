#Problem 21: Amicable numbers
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import sympy
from itertools import combinations
""" def divisors(num):
    return [x for x in range(1,num) if (num % x == 0)] """

def d(n):
    return sum(sympy.divisors(n))-n

amicable_cache = {}
def amicablePair(a,b):
    if (a,b) in amicable_cache:
        return amicable_cache[(a,b)]

    if d(a) == b and d(b) == a:
        amicable_cache[(a,b)] = True
        return True
    else:
        amicable_cache[(a,b)] = False
        return False

amicableNumbers = []
for (i,j) in combinations(range(1,10000),2):
    if amicablePair(i,j): 
        amicableNumbers.append(i)
        amicableNumbers.append(j)

#amicableNumbers = list(set(amicableNumbers))# reduce to unique amicable numbers

print(amicableNumbers)
answer = sum(amicableNumbers)
print(answer)