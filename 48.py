#Problem 48: Self powers
"""
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
@Author Max
"""

def seriesTo(num):
    return [i**i for i in range (1,num+1)]
    
answer = ''.join(list(str(sum(seriesTo(1000))))[-10:])
print(answer)