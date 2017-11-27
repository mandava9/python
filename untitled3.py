#name: Vivek Mandava
#date: 10/9/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 6a week 6
#ex 5
import math
n=int(input("Enter the number until which you need the primes: "))
i=2
primes= set([])
while i <= n:
	primes.add(i)
	i=i+1
j=2	
while j <= (math.sqrt(n)):
	for p in primes:
		if p % j=0:
			primes.discard(p)
print (primes) 