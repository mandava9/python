#name: Vivek Mandava
#date: 9/19/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 3b week 3

#Q4
# creating a list to enter the sales
list=[]
# initializing the total vairable
total = 0 
#sales = int(input("Enter the sales amount of the day: "))
#add ing the input into the list
for i in range(1,8):
    sales = int(input("Enter the sales amount of the day: "))
    list.append(sales)
    #updating total varialble 
    total= total+sales
    
#printing the list and the total for the week
print(list)
print("The total sales for the week is: "+str(total))
