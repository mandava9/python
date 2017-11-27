#To check for leap year(inclass)

year=int(input('Enter the year to checked : '))
if (year%400==0) or (year%100 != 0 and year % 4 == 0):
 	print("The year entered is an leap year")
else:
 	print("The year entered is not an leap year")

