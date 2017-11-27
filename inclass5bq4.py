#inclass lab 5a
#week5 q4

s1=str(input("Enter the first string "))
s2=str(input("Enter the second string "))

def hamming(a,b):
	if len(a) != len(b):
		return -1
	distance= 0
	for i in range(len(a)):
		if a[i] != b[i]:
			distance = distance +1
	return (distance)
print(hamming(s1,s2)) 