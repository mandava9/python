#q1 in class
number= int(input("Enter a number between 1 and 100: "))
while number <1 or number >100:
    print("Invalid entry. Please enter a number between 1 and 100 ")
    number= int(input("Enter a number between 1 and 100: "))
print("{:d} is the number you have entered".format(number))


#q2
days= int(input("Enter the number of days you have worked: "))
pay = 1
total = 0
for day in range(days):
     total= total + pay
     print("The pay for {:10d} day \t --> {:10d} pennis".format(day+1,pay))
     pay = pay*2
     
dollar= total/100
print("The total pay is $"+str(round(dollar,2)))

#q3
list=[]
total = 0 
new = int(input("Enter the positive number to be added to the list: "))
while new != -1:
    list.append(new)
    total= total+new
    new = int(input("Enter the positive number to be added to the list: "))

average = total/ len(list)
print(list)
print("The total of the numbers is: "+str(total)+" and the average of the numbers is: "+str(average))


#q4
rain_list= []
total=0
rain = int(input("Enter the rainfall in each month "))
for month in range(12):
    rain_list.append(rain)
    total= total + rain

#finding the minimum and maximum rainfal month
    
