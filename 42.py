#Problem 42: Coded triangle numbers
""" The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words? """
from string import ascii_lowercase

letsToNums = {}
i=1
for c in ascii_lowercase:
    letsToNums[c] = i
    i+=1

triNums = {1:1, 2:3, }
def triangleNumber(n):
    #memoized
    if n in triNums.keys():
        return triNums[n]
    else:
        ans = (n/2)*(n+1)
        triNums[n] = ans
        return int(ans)

def strToTriNums(s):
    wordVal = sum([letsToNums[c] for c in s])
    for (key,val) in zip(range(1,wordVal),[triangleNumber(n) for n in range(0,wordVal)]):
        if wordVal==val:
            return key 
        if wordVal < val: break #went too far
        #else: continue

with open("words.txt") as f:
    words = f.readline().split(",")#turn into list from csv
    words = [word.strip(' " " ').lower() for word in words]#remove quotes

print(len([strToTriNums(word) for word in words if strToTriNums(word) != None]))
print(len(words))
print([strToTriNums(word) for word in words if strToTriNums(word) != None])
#print(words)
print(strToTriNums("sky"))
#for some reason the answer is 162 not 161 words. :/