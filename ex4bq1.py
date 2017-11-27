#name: Vivek Mandava
#date: 9/25/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 4b week 4

#q1
#asking user for file name
file_name = input('Enter the name of the file: ')
n = int(input('Enter the number of lines to be printed from the file '))
f = open(file_name)
#using readlines function to store into a list
lines = f.readlines()
#length of the list
l = len(lines)
f.close()
#for loop to print last 'n' lines
for line in range(l-n-1,l):
	 print (lines[line])