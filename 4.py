#Problem 4: Largest palindrome product
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Q: Find the largest palindrome made from the product of two 3-digit numbers.
#plan:
#write function to check if a number is a palindrome
#make list of products between all 3 digit numbers
#sort from largest to smallest and check for first palindrome and report it

def palindromeCheck(num):
    num = list(str(num))
    reverseNum = list(reversed(num))
    if num == reverseNum:
        return True
    else:
        return False

# excluding leading zeros
allThreeDigitNumbers = [x for x in range(100,1000)]

#multiplies each number with every number after it
products = []
for x in range(0,len(allThreeDigitNumbers)-1):
    for y in range(x,len(allThreeDigitNumbers)-1):
        products.append(allThreeDigitNumbers[x]*allThreeDigitNumbers[y])
uniqueProducts = list(set(products)) # only unique products, e.g. 222*444 = 111*888 is duplicate

#get the largest first so we are done after finding first palindrome
uniqueProducts.sort()
uniqueProducts = list(reversed(uniqueProducts))

palindromes = []
i = 0
while i < len(uniqueProducts):
    x = uniqueProducts[i]
    if palindromeCheck(x):
        palindromes.append(x)
        break #sorted so we are done after we find the first
    else:
        i = i + 1

a = 345
b = 2112
print("is "+str(a)+" a palindrome? " +str(palindromeCheck(a)))
print("is "+str(b)+" a palindrome? " +str(palindromeCheck(b)))

#Solution to problem:
print("Largest 3 digit-product palindrome: "+str(palindromes[0]))

