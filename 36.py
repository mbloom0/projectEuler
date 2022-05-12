#Problem 36: Double-base palindromes
""" The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.) """
def decimalToBinary(n):
    return bin(n).replace("0b", "")

def palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

doublePalindrome = {}
for i in range(10**6):
    if palindrome(i) and palindrome(decimalToBinary(i)):
        doublePalindrome[i] = decimalToBinary(i)

print(doublePalindrome)
print(sum(doublePalindrome.keys()))