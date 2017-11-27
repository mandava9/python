#name: Vivek Mandava
#date: 10/2/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 5b week 5
#ex 3

sales=float(input("Enter the total sales for the month: "))
#function to calculate tax
def tax(a):
	'''Returns sales tax'''
	return("Country sales tax is $"+str(round((a*0.025),2))+" and the state sales tax for the month is $"+str(round((a*0.05),2))+" and the total sales tax is $"+str(round((a*0.075),2)))
#calling the function
print (tax(sales))