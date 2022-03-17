#Problem 5: Smallest multiple
#   2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#Q: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from functools import reduce
#plan:
# has to be at least divisible by all primes 1 to 20:
primes1to20 = [2,3,5,7,11,13,17,19]

def divisibleBy1to20(num):
    for i in list(reversed(range(1,21))):
        if num % i != 0:
            return False
    return True
#product of primes less than 20
solution = reduce((lambda x,y: x*y), primes1to20)

while not divisibleBy1to20(solution):
    solution+=1

#Solution to problem:
print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 without any remainder is: " + str(solution))
