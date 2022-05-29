#Problem 47: Distinct primes factors
"""The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each.
 What is the first of these numbers?"""

from sympy import factorint

for i in range(644, 1000000, 1):
    if len(factorint(i).keys()) == 4:
        if len(factorint(i+1).keys()) == 4:
            if len(factorint(i+2).keys()) == 4:
                if len(factorint(i+3).keys()) == 4:
                    print(i)
                    break
#wow, thanks github copilot! 