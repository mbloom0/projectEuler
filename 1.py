#problem from: https://projecteuler.net/problem=1
#finding all multiples of 3 or 5 under 1000
print(sum( list(filter(lambda x:x%3==0 or x%5==0,range(1000)) )))
