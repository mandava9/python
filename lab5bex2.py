#name: Vivek Mandava
#date: 10/2/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 5b week 5
#ex 2

import random
a=int(input("Enter a number between 1 and 100: "))
#generating random interger between 1 and 100
n=random.randint(1,101)
#function
def guess(i):
	'''Returns  if the entered number is close to the random number'''
	if i == n:
		return ("Congrats!!, you have guessed the number")
	elif i>n:
		return (" Too high, Try again!! ")
	elif i<n:
		return("Too low, Try again!! ")
#while loop to call the function 
while True:
	print(guess(a))
	a=int(input("Enter a number again between 1 and 100: "))
