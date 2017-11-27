#lab6aex3

gdp_values=dict()
f= open('world_gdp_data.txt')
lines=f.readlines()
f.close()
for line in lines:
	parts=line.split('|')
	gdp_values[parts[0]]=parts[1].strip()
#print(gdp_values)
name = str(input('Enter the name of the country to check the GDP(quit stops) '))
while name!= 'quit':
	if name in gdp_values.keys():
		print (name+" has a gdp of "+gdp_values[name])
	else:
		print('Not a valid country name')
	name = str(input('Enter the name of the country to check the GDP(quit stops) '))