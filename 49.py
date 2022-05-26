#Problem 49: Prime permutations
""" The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 
    3330, is unusual in two ways: (i) each of the three terms are prime, 
    and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting
    this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence? """
from math import floor
from sympy import isprime
from itertools import permutations

specialSequences = []

upper = 10**4
for (i,j) in [(i,j) for j in range(1,floor(upper/3)) for i in range(1000,upper-2*j +1)]:
    seq = [i,i+j,i+2*j]
    if seq[2] > 9999: continue
    if all(map(isprime,seq)):
        permuts = list(map(int,map(''.join,set(permutations(str(seq[0]),4)))))
        if (seq[1] in permuts) and (seq[2] in permuts):#check for permutations
            specialSequences.append((seq,"y = "+str(i)+"+x"+str(j)+""))

print(specialSequences)
