#Problem 34: Digit factorials
""" 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included. """
from math import factorial
print(factorial(9)+factorial(9)+factorial(9)+factorial(9)+factorial(9)+factorial(9)+factorial(9)+factorial(9))
#from some quick teting of adding factoails of the greatest posible digit for each digit in the number (9), after
# about 8 digits, the sum of the factorials is less than the lenght of the number so this is about our limit
""" Attempt 1
def numEqSumFacDig(n):
    n = str(n)
    if sum([factorial(int(x)) for x in n]) == int(n):
        return True
    return False

allNumsWhosDigitsSumFactorially = []
for i in range(10**9):
    if numEqSumFacDig(i):
        print(i)
        allNumsWhosDigitsSumFactorially.append(i)

print(sum(allNumsWhosDigitsSumFactorially)) """
nums = []
i = 3
while i < 10**6: #turns out it is 6 not 5, also this is constructive not destructive
    s = sum([factorial(int(x)) for x in str(i)])
    if i == s: 
        nums.append(s)
        print(s)
    i +=1

print(sum(nums))