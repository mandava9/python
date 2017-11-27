# week 4 in class Q4 to calculate the total of quizzes
f = open('quizzes.txt')
lines = f.readlines()
f.close()
g= open('wuiz_average.txt','w')
for line in lines:
	sum = 0
	line= line.strip()
	parts = line.split()
	for score in parts[2:]:
		sum = sum + int(score)
	average = sum / len(parts[2:])
	g.write(line +str(average))
g.close()
