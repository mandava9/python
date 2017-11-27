#inclass lab 5a
#week5 q2

strng=str(input("Enter the string "))
def count_vowels(stng):
	'''Returns the number of vowels in the string'''
	stng=stng.lower()
	t=0
	for i in range(len(stng)):
		if stng[i] == 'a' or stng[i] == 'e' or stng[i] == 'i' or stng[i] == 'o' or stng[i] == 'u':
			t = t+1
	return (t)
print(count_vowels(strng))

###### Alternate method
#vowels='aeiou'
#for l in s:
	#if letter in vowels:
		#count= count+1
#return(count)