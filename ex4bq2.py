#name: Vivek Mandava
#date: 9/25/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 4b week 4

#Q2
#reading input file
f = open('jan_wx.txt')
#saving into a list of lines
lines = f.readlines()
f.close()
#writing output into a file
g= open('jan_wx_metric.txt','w')
#for loop to change snow fall height @index 1 and temperature @index2 in the input file
for i in range(0,31):
	 new_line=(lines[i].split())
	 new_line[1]=round(float(new_line[1])*2.54,1)
	 new_line[2]=round((float(new_line[2])-32)*5/9,1)
	 #for loop to write each line in the output file
	 for j in range(5):
	 	 g.write(str(new_line[j])+" ")
	 #to print in next line
	 g.write("\n")
g.close()