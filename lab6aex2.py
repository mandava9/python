#lab6aex2

try:
	f = open('college.txt')
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
print(words)
words=set(words)
words=list(words)
words.sort()
print(words)
print(len(words))