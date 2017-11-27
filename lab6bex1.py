#name: Vivek Mandava
#date: 10/8/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 6b week 6
#ex 1
rooms={'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
instructors={'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
times={'CS101':'8:00 am','CS102':'9:00 am','CS103':'10:00 am','NT110':'11:00 am','CM241':'1:00 pm'}
course=str(input("Enter the course number: "))
print (str(course)+" is in room number "+str(rooms[course])+" and is taught by "+str(instructors[course])+" at "+str(times[course]))