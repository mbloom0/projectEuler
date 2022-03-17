#Problem 6:Sum square difference
#The sum of the squares of the first ten natural numbers is 1^2+2^2+...+10^2 = 385
#The square of the sum of the first ten natural numbers is (1+2+...+10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#plan: Answer is square of sum less sum of squares
inList = range(1,101) #[1,2,...,100]
#Solution to problem:
solution = sum(inList)**2 - sum(map((lambda x: x**2),inList))
print("The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is: " + str(solution))
