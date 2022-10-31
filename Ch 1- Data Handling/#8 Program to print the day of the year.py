'''
Question- Write a program to take two inputs for day, month and then calculate which day of the year, the given date is.
For simplicity ,take 30 days for all months.
For example ,if you give input as : Day 3 month 2 then it should print "day of the year : 33".
'''
#Solution

day=int(input("Enter the day of the month"))
month=int(input("Enter the month number"))

print("Day of the year :",month*30+day)
