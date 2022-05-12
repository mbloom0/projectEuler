import numpy as np
from math import sqrt
from math import ceil
from math import floor

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.
cap = 2000000

# generate 2d array containining numbers 1 to cap
n = ceil(sqrt(cap))
primeArray = np.zeros((n,n))
for x in range(n):#length
    primeArray[x-1] = range(1+(x*n), 1+((x+1)*n))#fill out each row

#consider every number from 2 to the cap
for x in range(1,cap):
    x=x+1 #start 2
    #if number is still prime candidate
    if x != 0:
        #remove (set to 0) every multiple of the number to the cap
        for y in range(x,cap):
            if y%x==0:
                primeArray[floor(y/n),y%n] = 0

print("Sum of all primes less than 2million: ", np.sum(primeArray) )
