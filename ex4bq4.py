#name: Vivek Mandava
#date: 9/26/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 4b week 4

#Q4
#opening input
f = open('test4bq3.txt')
#storing lines into a list
lines = f.readlines()
f.close()
#printing the length of list gives the number of lines
print ("The total number of elements are "+str(len(lines)))
total=0
#for lopp to add all the numbers
for i in range(len(lines)):
	 total=total + int(lines[i])
print ("The total of the random numbers is "+str(total))