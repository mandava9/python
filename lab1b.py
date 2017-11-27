#1

#taking input
name=input('Q1: Enter your name  ')
#printing
print('Hello and welcome '+str(name)+' !')



#2

#taking input
price=float(input('Q2: Enter the cost  of the food '))
#calculating total price
cost = price + (0.18 * price ) + (0.095 * price)
print('The total amout to be paid is $' + str(cost))



#3
#taking to convert in celsius
tempc=float(input('Q3: Enter the temperature in Celsius '))
#formula
tempf = ((9 * tempc )/5)+ 32
print ('The converted temperature in Fahrenheit is '+ str(tempf))



 #4

boys=int(input('Q4: Enter the number of Boys in class '))
girls=int(input('Enter the number of Girls in class '))
#calculating total
total = boys + girls 
#percentage formula
pboys = ( boys / total )* 100
#rest is girls
pgirls= 100 - pboys
print(' '+str(round(pboys,2)) + '% of the class are boys and '+ str(round(pgirls,2)) +'% are girls ' )



#5

# miles, feet and inches
#taking weight to convert
meters = float(input('Q5: Enter distance in meters ') ) 
	# meter = 0.000621371 miles. 1 mile = 5280 feet. 1 foot = 12 inches
	#converting to miles using formula
mile = meters * 0.000621371 
#converting to feet
feet= mile * 5280  
# we cant have decimal point in feet
#multiplying with ten to get the decimal part of the feet.
feet = round(feet,1)
feet = feet * 10
#than getting the remainder
inc = feet % 10
# reseting the value of the feet
feet = round(feet,0)
feet = feet / 10
#dividing the remainder again to get just the decimal part of the feet
inch = inc / 10
#converting the decimal of feet into inches
inches = inch * 12
#printing the values
print('the converted values are '+str(mile)+' miles and '+str(round(feet,0))+' Feet '+str(round(inches,2))+' inches')
