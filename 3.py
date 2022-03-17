#Project euler program to solve problem number 3: Largest Prime Factor.
#The prime factors of 13195 are 5, 7, 13 and 29.
#Q: What is the largest prime factor of the number 600851475143?

import numpy 
import math
number = 600851475143

#found on stackoverflow https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primesfrom3to(n):
    """ Returns an array of primes, 3 <= p < n """
    sieve = numpy.ones(math.ceil(math.sqrt(n)), dtype=bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

def primeFactorize(num):
    primes = primesfrom3to(math.ceil(num/2))
    factors = [x for x in primes if (num%x==0)]
    return factors

def main():
    #print(list(prime2(number)))
    print("Prime factors of "+str(number)+": ")
    print(primeFactorize(number))

if __name__=="__main__":
    main()
