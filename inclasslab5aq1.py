#inclass lab 5a
#week5

n=int(input("Enter the first number "))
m=int(input("Enter the second number "))

def max(a,b):
	'''Returns the maximum number'''
	if a>b:
		return(n," is the maximum number")
	else:
		return(m," is the maximum number")
print(max(n,m))