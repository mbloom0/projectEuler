import numpy as np
import csv
import math
#Largest exponential
  #Problem 99
#Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.
#However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.
#Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

with open('base_exp.txt') as file_obj:
    reader_obj=csv.reader(file_obj)
    base_exp = [] 
    for row in reader_obj:
        base_exp.append(row)    
#actual answer "i" from this answers list = e**answer[i], log used to reduce number size with properties
answers = [math.log(int(x[0]))* int(x[1]) for x in base_exp]
for x in range(len(answers)):
    answers[x] = (answers[x],x)

answers.sort(key=lambda x: x[0])

print(answers)
#Last answer's index +1 = line number = answer to problem
