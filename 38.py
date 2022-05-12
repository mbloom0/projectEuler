#Problem 38: Pandigital multiples
""" Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1? """
from itertools import permutations

def concatenatedProduct(n, multiplicands):
    return int(''.join(map(str,[n*m for m in multiplicands])))

perms = permutations("123456789")#['1','2','3','4','5','6','7','8','9'])
print(list(map(''.join,perms)))
def pandigital(n): #9 digit 1 thru 9 pandigital
    if len(n) != 9: return False
    n = [digit for digit in n]
    n.sort()
    i=0
    for c in n:
        if c != "123456789"[i]:
            return False
        i+=1
    return True
"""
    if n == str((range(1,len(n)))):
        return True
    else:
        return False
#differnt strat 
    for c in '123456789':
        if c in n and n.count(c) == 1:
            continue
        else:
            return False
    return True
#another strat 
    if n in map(''.join,perms):
        return True
    else:
        return False
"""
largest = 0
k=0
for i in range(1,10**4):
    for j in range(1,10**2):
        lol = concatenatedProduct(i,range(j))
        if pandigital(str(lol)) and lol > largest:
            largest = lol
        if len(str(lol)) > 9: k+=1
        if len(str(lol))*k > 9000: break

print(largest)
