#Problem 14: Longest Collatz sequence
#The following iterative sequence is defined for the set of positive integers:
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#Which starting number, under one million, produces the longest chain?
#NOTE: Once the chain starts the terms are allowed to go above one million.


def collatzSeq(seed):
    """Generates list containing Collatz sequence beginning from seed"""
    chain = [seed]
    n = seed
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        chain.append(n)
    return chain

#measure length of collatz sequences from first million seeds
colSeqLen = []
for i in range(1,10**6):
    colSeqLen.append(len(collatzSeq(i)))

longestSequence = max(colSeqLen)
longestSeed = colSeqLen.index(longestSequence) + 1 #solution
#Print solution
print("Longest Collatz sequence starting from a seed under 1 million: " + str(longestSeed))
print("or " + str(colSeqLen.index(max(colSeqLen)) +1 )  )
