#name: Vivek Mandava
#date: 9/19/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 3b week 3

#Q2
#asking the user to enter an exchange rate
exchange_rate= float(input(" Enter the exchange rate for today "))
# taking the amount in dollars that is to be converted
dollar = float(input(" Enter amount to be converted into rupees: "))
# if the dollar value is 0 the program ends
while dollar != 0:
	rupee = dollar * exchange_rate
	print("The value in rupees is Rs. "+str(rupee))
	dollar = float(input(" Enter amount to be converted into rupees: "))