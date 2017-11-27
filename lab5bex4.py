#name: Vivek Mandava
#date: 10/2/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 5b week 5
#ex 4
#importing the library re to use re.findall() function
import re
#function to check the password
def check_password(password):
	#length check
	if len(password) < 8:
		return("Make sure your password is at lest 8 letters")
	#checking for uppercase letters using the function findall
	if len(re.findall(r'([A-Z])',password)) == 0:
		return("Make sure your password has a uppercase in it")
	##checking for lowercase letters using the function findall
	if len(re.findall(r'([a-z])',password)) == 0:
		return("Make sure your password has a lowercase in it")
	#checking for a number using the function findall
	if len(re.findall(r'([\d])',password)) == 0:
		return("Make sure your password has one number in it")
	else:
		return("Your password meets the requirement")
#while loop to repeat the function
while True:
	password=str(input("Enter the password, that is to be checked "))
	print(check_password(password))
