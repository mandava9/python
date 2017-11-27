#name: Vivek Mandava
#date: 9/26/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 4b week 4

#Q3

import random
#asking user for the number of random numbers
n = int(input("Enter the number of random numbers you want in the file "))
#output file
g= open('test4bq3.txt','w')
#writing in outputfile
for i in range(n):
	 rand=(random.randint(1,500))
	 g.write(str(rand)+"\n")
g.close()
