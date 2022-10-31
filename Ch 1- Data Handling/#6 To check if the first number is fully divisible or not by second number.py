#Question-Write a program to take two number and print if the first number is fully divisible by the second number or not.

#Solution-

first_number=int(input("Enter the first number"))
second_number=int(input("Enter the second number"))

if first_number%second_number==0:
	print (f"{first_number} is fully divisible by {second_number}")
else:
	print (f"{first_number} is not fully divisible by {second_number}")