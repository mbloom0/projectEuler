#Problem 23: Non-abundant sums
"""A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum 
of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two 
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as 
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is 
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

@Author Max
"""

import sympy

def abundant(num):
    """Returns true if num is abundant. Num is abundant if the sum of it's perfect divisors is greater than itself."""
    if (sum(sympy.divisors(num))-num) > num:
        return True
    else:
        return False

def sumOfAbundants(num):
    """returns true if num can be written as sum of two abundant numbers"""
    for i in range(12,num+1):
        j = num - i
        if abundant(i) and abundant(j) and i+j==num:
            return True
    return False

notSumsOfAbundants = [x for x in range(1,28123+1) if not sumOfAbundants(x)]
answer = sum(notSumsOfAbundants)
print(answer)


