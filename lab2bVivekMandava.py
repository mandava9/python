#name: Vivek Mandava
#date: 9/6/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 2b week 2

#Q1 Temperature of water
temp = float(inout('Enter the temperature of water in celsius'))
if temp <= 0:
	print("Water is in ICE form i.e Solid")
elif temp > 0 < 100:
	print("Water is in Liquid form")
elif temp >= 100:
	print("water is in vapor form, i.e in gas form")
elif temp == 0:
	print("This is called freezing point of water.")
elif temp == 100:
	print("This is called boiling point of water. ")
