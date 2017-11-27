#name: Vivek Mandava
#date: 9/20/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 3b week 3

#Q2
#importing math library
import math
#taking input from the user to set the range
n = int(input(" Enter a number, until which you want the prime numbers: "))                                                  
print('The prime numbers between 2 and '+str(n)+  ' are the following:')
#validation of the input
if n > 1:
    for i in range(2, n+1):
    # Assume i is prime
        prime = True
    # The last possible multiple we
    # need to check is the square root of i.
    # Use int() to convert the float output
    # of math.sqrt() to int, since range()
    # requires both the lower and upper
    # limits to be of type int
        upper_limit = int(math.sqrt(i)) + 1
        for j in range(2, upper_limit):
        # If j evenly divides i, then
        # i is not a prime number
            if i % j == 0:
                prime = False
        if prime:
            print(i)
# validating the input and asking the used to enter a valid input
else :
    n = int(input(" Enter a number greater than 1: "))
