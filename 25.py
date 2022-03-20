#Problem 25: 1000-digit Fibonacci number
"""The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
The 12th term, F12, is the first term to contain three digits.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
@Author Max
"""

fibonacci_cache = {1:1,
2:1}
def fibonacci(n):
    """memoized fibonacci number generator"""
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    fibN = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = fibN 
    return fibN

#stop and print index when fib number length > 999 digits (==1000 digits)
num = 1
while len(str(fibonacci(num))) < 1000:
    num += 1

print(num)#answer
