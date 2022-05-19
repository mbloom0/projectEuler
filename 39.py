#Problem 39: Integer right triangles
""" If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there
are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised? """
#we know
#p = a+b+c
#c**2 = a**2 + b**2
#two equations, three variables so "infinite" solutions, # limited by # of integer solutions

#let x=a, y=b
#then y= (p(x-p/2))/(x-p)
from math import sqrt
combosForDiffPerims={} #(perim: triangles(x,y) that make p)

for p in range(12,1001):
    triangleSides = []#collect (a,b,c) for each value of p
    for x in range(1,p):
        numerator= p*(x-(p/2))
        denominator = x-p
        if numerator%denominator ==0:#only collect if evenly divisible (integer solutions)
            y = numerator/denominator
            if y<=0:continue #do not want side lengths that are zero or negative 
            triangleSides.append((x,y,sqrt(x**2 +y**2)))
    combosForDiffPerims[p]=triangleSides

#note, some solutions are redundant: where and b are swapped

#
for item in combosForDiffPerims.items():
    if len(item[1]) == max(map(len,combosForDiffPerims.values())):
        print(item)
