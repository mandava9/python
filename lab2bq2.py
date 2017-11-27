#author: Vivek Mandava
#date: 9/8/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 2b week 2
#Q2 Comparing 3 numbers
#taking input to compare the numbers
a = int(input('Enter the first number  '))
b = int(input('Enter the second number  '))
c = int(input('Enter the third number  '))
#checking if the numbers are equal
if a==b==c:
	print("The three numbers are same")
# checking if all the numbers are different
elif a!=b and b!=c and c!=a:
	print("The three numbers are different")
# the remaining numbers are neither
else :
	print("Neither")
