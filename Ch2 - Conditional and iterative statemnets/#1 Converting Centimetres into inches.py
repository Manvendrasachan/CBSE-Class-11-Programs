'''
Write a Python script that asks the user to enter a length in centimetres. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program should convert
the length to inches and print out the result. There are 2.54 centimetres in an inch.
'''
#Solution-

centimetres=int(input("Enter the lenght in centimetres"))
if (centimetres>=-1):
	print (f"{centimetres} is equal to",centimetres/2.54,"inches")
else:
	print ("Entry is invalid")
