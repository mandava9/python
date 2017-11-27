#name: Vivek Mandava
#date: 9/20/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 3b week 3

#Q5
#creting a list
list=[]
#for loop to take input from the user
for i in range(10):
	new = int(input("Enter a number to be added to the list: "))
	#using append to add values into the list
	list.append(new)
#to print all the elements at even index, i.e the elements at odd computer index, using j as an index
j=1
print("All the emelents in even index are: ")
while j < 10 :
	print (list[j])
	j=j+2
# to print all the even elements
print("All the even elements are: ")
for k in range(10):
# checking for even number by dividing the number by 2 and checking if the remainder is 0
	if list[k]%2==0:
		print (list[k])
# printing all the elements in reverse order
print("All the elements in reverse order, are: ")	
#using the reversed function to reverse the list	
for l in reversed(list):
	print (l)
# printing the first and last elements as we know the length of the array
print("The first element is: ")
print(list[0])
print("The last element is: ")
print(list[9])
