#inclass lab 5a
#week5 q2

word=str(input("Enter the word to be checked "))
def check_palin(s):
	s=s.lower()
	l=len(s)
	for i in range(l):
		if s[i] == s[l-i-1]:
			return("The word entered is a palindrome")
		else:
			return("The given word is not a palindrome")
print(check_palin(word))


##### ********** Solution **************
#def check_palindrome():
#t = '' #empty string
#for letter in s:
	#if letter.isalpha():
		#t = t+letter
#if len(t)>0 and t == t[::-1]:
	#return true
#return false