# In class week 2 lab2a


#1

x= int(input('Enter an interger to check if it is positive or negative '))
if x < 0:
 print("The number is negative")
else:
 print("The number is positive")



#2

y= int(input('Enter an interger between 1 to 7'))
if y==1:
	print("Its Monday")

elif y==2:
    print("Its Tuesday")

elif y==3:
	print("Its Wednesday")

elif y==4:
	print("Its Thursday")

elif y==5:
	print("Its Friday")

elif y==6:
	print("Its Saturday")

elif y==7:
	print("Its Sunday")

else:
	print("The number entered is outside of the range")



#3

year=int(input('Enter the year to checked'))
if year%100 == 0 and year%400==0:
 	print("The year entered is an leap year")

elif year%100 != 0 and year % 4 == 0:
        print("The year entered is an leap year")

else:
 	print("The year entered is not an leap year")


#4

number = int(input('Enter a number between 1 and 10'))
if number == 1:
	print("The roamn version of 1 is I")
elif number ==2:
	print("The roamn version of 2 is II")
elif number ==3:
	print("The roamn version of 3 is III")
elif number ==4:
	print("The roamn version of 4 is IV")
elif number ==5:
	print("The roamn version of 5 is V")
elif number ==6:
	print("The roamn version of 6 is VI")
elif number ==7:
	print("The roamn version of 7 is VII")
elif number ==8:
	print("The roamn version of 8 is VIII")
elif number ==9:
	print("The roamn version of 9 is IX")
elif number ==10:
	print("The roamn version of 10 is X")
else:
	print("The number entered is not in range")


#5

mon = int(input('Enter a number month between 1 and 12'))
if mon == 1 or mon == 3 or mon ==5 or mon ==7 or mon==8 or mon==10 or mon == 12:
	print("The number of days in this month are 31")
elif mon == 2:
	print("The number of days in Feb are 28 or 29")
elif mon == 4 or mon == 6 or mon ==9 or mon ==11:
	print("The number of days in this month are 30")
	


