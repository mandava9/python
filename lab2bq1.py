#name: Vivek Mandava
#date: 9/6/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 2b week 2

#Q1 Temperature of water
#taking input for checking the state of water
temp = int(input('Enter the temperature of water in celsius  '))
# water is in ice form below 0
if temp < 0:
	print("Water is in ICE form i.e Solid")
#condition for water in gases form
elif temp>100:
	print("Water is in vapor form, i.e in gas form")
#100 degree c is called boiling point of water where it turns into vapor
elif temp == 100:
	print("This is called boiling point of water. ")
#This is called freezing point or melting point
elif temp == 0:
	print("This is called freezing point of water.")
# contion for water in liquid state 
elif temp>0 and temp<100:
	print("Water is in Liquid form")



