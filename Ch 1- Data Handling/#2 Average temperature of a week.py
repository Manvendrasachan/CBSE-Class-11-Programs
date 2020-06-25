'''Question- write a program to obtain temperature of 7 days and then display average temperature of
the week'''
# Solution
temp=[]
days=("monday","tuesday","wednesday","thrusday","friday","saturday","sunday")
for j in range(7):
	temperature=int(input(("enter the max terperature of",days[j])))
	temp=temp+[temperature]
print("average temperature is =",(sum(temp)/7))
