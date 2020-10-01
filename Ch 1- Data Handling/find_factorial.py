#give an integer as an input and find the factorial of given number.
num=int(input())
def fact(num):
  if num==0:
    return 1
  return num*fact(num-1)
