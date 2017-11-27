#name: Vivek Mandava
#date: 9/18/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 3b week 3

#Q1
#creating a list 
list=[]
index = 0
#fo loop to add elements to the list
for index in range(10):
	new = int(input("Enter the number to be added to the list: "))
	#using append function to add elements to the list
	list.append(new)
	index = index + 1
# for loop to print the elements in reverse order by using the reversed function
for index2 in reversed(list):
	print (index2)