#q1
file_name = input('Enter the name of the file: ')
f = open(file_name)
lines = f.readlines()
f.close()
for line in lines[:5]:
	print (line.strip())

#Q2
f= open('mending_wall.txt')
chars = f.read()
chars = chars.lower()
f.close()
vowels = ('a','e,','i','o','u')
counts = [0,0,0,0,0]
total = 0
for char in chars:
	if char in vowels:
		pos = vowels.index(char)
		counts[pos]=counts[pos]+1
		total = total + 1
for i in range(len(vowels)):
	print(vowels[i]+':',counts[i])
print('The total number of vowels are'+str(total))

#q3
