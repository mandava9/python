#author: Vivek Mandava
#date: 9/11/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 2b week 2

#Q5 color of the pocket on the roulette wheel
#input for the program
num = int(input('Enter the number between 0 and 36  '))
# checking if the number is in the range
if num < 0 or num > 36:
        print("Please enter the number between 0 and 36")
# condition for green i.e 0
elif num == 0:
        print("The color of the pocket is Green ")
# all the numbers that are in red pockets
elif num == 1 or num == 3 or num == 5 or num == 7 or num == 9 or num == 12 or num == 14 or num == 16 or num == 18 or num == 19 or num == 21 or num == 23 or num == 25 or num == 27 or num == 30 or num == 32 or num == 34 or num == 36:
        print("The color of the pocket is Red")
#the rest between 0 and 36 are black
else:
        print("The color of the pocket is Black")
