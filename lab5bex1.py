#name: Vivek Mandava
#date: 10/2/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 5b week 5
#ex1

n=int(input("Enter the number that is to be checked: "))
#declaring function
def is_even(a):
	'''Returns true if even number number and false if odd'''
	#checking for even number
	if a%2 == 0:
		return ("true")
	else:
		return ("false")
#printing if the number is even or odd
if is_even(n) == ("true"):
	print("The number "+ str(n) +" is an even number")
else:
	print("The number "+ str(n)+ " is an odd number")