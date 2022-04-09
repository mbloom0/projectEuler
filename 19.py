#Problem 19: Counting Sundays
""" You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
from  datetime import date, timedelta
start_date = date(1901, 1, 1)  
end_date = date(2000, 12, 31)   
delta = end_date - start_date   

answer = [(start_date + timedelta(days=x)) for x in range(0,delta.days + 1) 
        if (start_date + timedelta(days=x)).strftime("%A") == "Sunday" 
            and (start_date + timedelta(days=x)).day == 1
         ]

print(len(answer))
