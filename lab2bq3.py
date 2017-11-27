#author: Vivek Mandava
#date: 9/8/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 2b week 2

#Q3 Check for magic date
#taking date input from the user
date = int(input('Enter the date  '))
month = int(input('Enter the month in number between 1 and 12  '))
year = int(input('Enter the two digit year  '))
# only 12 months so asking the user tp enter with in the range
if month > 12:
        print("Please enter the month between 1 and 12")
# for the months that have 31 days in them
elif (month == 1 or month==3 or month==5 or month==7 or month==8 or month == 10 or month == 12) and date >31:
        print("Please enter the date for this month between 1 and 31")
# for the months that have 30 days in them
elif (month == 4 or month==6 or month==9 or month==11) and date >30:
        print("Please enter the date for this month between 1 and 30")
# for feb which has only 28 or 29 days
elif month == 2 and date >29:
        print("Please enter the date for this month between 1 and 29")
# year can be only in 2 digit
elif year > 99 or year < 0:
        print("Please enter the date for this year between 1 and 99")
#condition to check for magic year
elif month*date==year:
	print("This is a magic date")
# the rest are not magic
else :
	print("This date is not a magic date")


