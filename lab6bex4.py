#name: Vivek Mandava
#date: 10/10/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 6b week 6
#ex 4
filename=input("Enter the file name to be opened ")
try:
	f = open(filename)
except FileNotFoundError:
	print("File not found")
	sys.exit(1)
content = f.read()
f.close()
for char in content:
	if not char.isalpha()and char != ' ':
		content=content.replace(char,' ')
content=content.lower()
words=content.split()
worddic= {}
for w in words:
	if w not in worddic:
		worddic[w] = 0
	worddic[w] = worddic[w] + 1
print(worddic)