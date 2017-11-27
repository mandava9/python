#name: Vivek Mandava
#date: 9/26/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 4b week 4

#Q5
import sys
#try block 
try:
     #opening input file
     f = open('test4bq3.txt')
     lines = f.readlines()
     f.close()
     print ("The total number of elements are "+str(len(lines)))
     total=0
     for i in range(len(lines)):
        total=total + int(lines[i])
     print ("The total of the random numbers is "+str(total))
#exception if the input file is not found
except IOError as e:
    errno, strerror = e.args
    print("I/O error({0}): {1}".format(errno,strerror))
#exception if the input is not int
except ValueError:
    print("No valid integer in line.")
#else unexpected error and raise
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
