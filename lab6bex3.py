#name: Vivek Mandava
#date: 10/10/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 6b week 6
#ex 3
def quiz():
    capitals = {'Austria':'Vienna','Belgium':'Brussels','Bulgaria':'Sofia','Croatia':'Zagreb','Cyprus':'Nicosia','Czech Republic':'Prague','Denmark':'Copenhagen','Estonia':'Tallinn','Finland':'Helsinki','France':'Paris','Germany':'Berlin','Greece':'Athens','Hungary':'Budapest','Ireland':'Dublin','Italy':'Rome','Latvia':'Riga','Lithuania':'Vilnius','Luxembourg':'Luxembourg','Malta':'Valletta','Netherlands':'Amsterdam','Poland':'Warsaw','Portugal':'Lisbon','Romania':'Bucharest','Slovakia':'Bratislava','Slovenia':'Ljubljana','Spain':'Madrid','Sweden':'Stockholm','United Kingdom':'London'}
    correct = 0
    wrong = 0
    for cap in capitals.keys():
    	answer = input('What is the capital of '+cap)
    	if answer.upper() == capitals[cap].upper():
    		correct = correct + 1
    		print('Correct Answer, Congrats')
    	else:
    		wrong = wrong + 1
    		print('Wrong Answer')
    print("Number of correct answers are: "+str(correct))
    print("Number of incorrect answers is:"+ str(wrong))
quiz()