#name: Vivek Mandava
#date: 10/9/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 6a week 6
#ex 5
#importing math to calculate square root of a number
import math
#taking input form the user to calculate primes
n=int(input("Enter the number until which you need the primes: "))
i=2
#initializing a set called primes
primes= set([])
#while loop to add 2 to n numbers in the set
while i <= n:
	primes.add(i)
	i=i+1
j=2	
# eleminating all numbers that are divisible by any number other than the number itself
while j <= (math.sqrt(n)):
	for p in range(2,(n+1)):
		if p % j == 0 and p/j!=1:
			primes.discard(p)
	j=j+1
#printing the set with all prime numbers untill n
print ("All the prime numbers until "+str(n)+" are "+str(primes))