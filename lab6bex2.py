#name: Vivek Mandava
#date: 10/10/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 6b week 6
#ex 2

try:
	f = open('world_gdp_data.txt')
except FileNotFoundError:
	print("File not found")
	sys.exit(1)
lines = f.readlines()
gdp = {}
for line in lines:
	line=line.split("|")
	gdp[line[0]]=line[1]
letter=str(input("Enter a letter: "))
letter=letter.upper()
temp={}
for key in gdp:
	key1 = str(key)
	key1=key1.upper()
	if letter in key1[0]:
		print(key1)
		print(gdp[key])