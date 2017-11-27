#inclass lab 5a
#week5 q5

def falling_distance(t):
	g=9.8
	return (g*t*t*0.5)
for i in range(1,11):
	print(falling_distance(i))