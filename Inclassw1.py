# 1
name = "Hello, My name is Vivek Mandava."
city = " I was born in Vijayawada."
team = " My favourite sports team is Real Madrid"
major = " I did my undergraduation in Computer Science"
print (name + city + team + major)

# 2
gross = eval(input('Enter the gross sales of the company: '))
profit = (gross) * (0.23)
print (profit)

#3
item1 = float(input('Enter the value of the first item: '))
item2 = float(input('Enter the value of the second item: '))
item3 = float(input('Enter the value of the third item: '))
subtotal= item1 + item2 + item3
tax = (0.06) * (subtotal)
total = tax + subtotal
print('Value of the items is $' + str(subtotal) + ' Tax amount is $' + str(tax) + ' Total sum is $' + str(total)+'.')


#4
speed = 65
time1 = 6
time2 = 10
time3 = 15
distance1 = speed * time1
distance2 = speed * time2
distance3 = speed * time3
print('The distance the car travelled by the car in 6 hours at 65 MPH is '+ str(distance1)+' Miles')
print('The distance the car travelled by the car in 10 hours at 65 MPH is '+ str(distance2)+' Miles')
print('The distance the car travelled by the car in 15 hours at 65 MPH is '+ str(distance3)+' Miles')


#5
miles = float(input(' Enter the miles driven on the car: '))
gas = float(input(' Enter the gallons of gas used for the car: '))
mpg = miles / gas
print(' The fuel economy of the car is ' + str(mpg) + 'MPG')
