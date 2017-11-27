#name: Vivek Mandava
#date: 10/2/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 5b week 5
#ex 5

#taking 5 score from the user
i= float(input("Enter the first score: "))
j= float(input("Enter the second score: "))
k= float(input("Enter the third score: "))
l= float(input("Enter the fourth score: "))
m= float(input("Enter the fifth score: "))
#function to calculate average
def calc_average(a,b,c,d,e):
	average=0
	average = (a+b+c+d+e)/5
	return(average)
print("The average of scores is "+str(round(calc_average(i,j,k,l,m),2)))

#function to calculate grade
def determine_grade(a):
	#if conditions for grades
	if a >=90:
		return("It's an A")
	if a >=80 and a <= 89:
		return("It's a B")
	if a >=70 and a <= 79:
		return("It's a C")
	if a >=60 and a <= 69:
		return("It's a D")
	if a <60:
		return("It's an F")
#storing the scores into a list
list=[i,j,k,l,m]
print("Following are the grades for 5 courses:\n")
#using a for loop to print the grades for all 5 scores
for lis in list:
	print(determine_grade(lis))