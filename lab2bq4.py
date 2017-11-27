#author: Vivek Mandava
#date: 9/11/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 2b week 2

#Q4 calculate employee pay
#taking input from the user for calculating total wage
wage = float(input('Enter the hourly wage in dollars  '))
hours = float(input('Enter the hours weekly  '))

# if the hours are less than 40 
if hours < 40 or hours== 40:
        total = wage*hours
        print("Pay for the employee is $"+str(round(total,2)))
#if the employees works more than 40 hours
elif hours > 40:
#calculating the overtime hours
        ot = hours - 40
        total = (40 * wage )+(ot*wage*1.5)
        print("Pay for the employee is $"+str(round(total,2)))
#exception
else
        print("Enter a correct amount")
