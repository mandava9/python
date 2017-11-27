#name: Vivek Mandava
#date: 10/10/2017
#email: VMandava_GPS@nec.edu
#purpose: Take home lab 6b week 6
#ex 5


import pickle

def run_menu():
    '''Displays program menu and returns the user's
       choice as a lowercase letter  to the caller.'''
    # Valid choices are 'a' for add, 'e' for edit,
    # 'd' for delete, 'l' for lookup, and 'q' to quit
    valid_choices = 'aedlq'
    # Set a flag variable to be used to signal
    # that a valid choice has been made. Flag
    # will be set to True when that happens
    done = False
    while not done:
        print('\nMonty Python\'s Email Contact List Program\n')
        print('Menu\n')
        print('(A)dd a Contact')
        print('(E)dit a Contact')
        print('(D)elete a Contact')
        print('(L)ook up a Contact')
        print('(Q)uit\n')
        choice = input('Your choice: ')
        # Force choice to lowercase so
        # the caller doesn't have to
        # also handle uppercase letters
        choice = choice.lower()
        if choice in valid_choices:
            return choice
        else:
            print('Sorry, that\'s not a valid choice!')
            input('Press <Enter> to continue...')
            print()
            
def add_contact(contacts):
    '''Prompts the user for a contact name
       and email to add, then adds the new
       contact to the provided contacts 
       dictionary.'''
    # Replace the line below with your code
    # to add a contact to the dictionary
    # passed into the function
    print('Add contact')
    newname = input("Enter name to be added to the list: ") 
    newname=newname.lower()
    newemail = input("Enter the email address of the contact: ") 
    newemail=newemail.lower()
    contacts.update({newname : newemail})

def edit_contact(contacts):
    '''Prompts the user for a contact name
       and email to edit, then prompts for
       a new email address for that contact
       in the provided contacts dictionary.'''
    # Replace the line below with your code
    # to edit a contact in the dictionary
    
    print('Edit contact')
    editname = input("Enter the name of contact that is to be edited: ")
    editname=editname.lower()
    newemail = input("Enter the new email address of the contact: ") 
    newemail=newemail.lower()
    contacts[editname] = new_email 
    print("The new email addres for "+editname+" is "+contacts[editname])
                      

def delete_contact(contacts):
    '''Prompts the user for a contact name
       and email to deleted, then removes the
       contact from the provided contacts
       dictionary.'''
    # Replace the line below with your code
    # to delete a contact from the dictionary
    # passed into the function
    print('Delete contact')
    deletename = input("Enter the name of the contact you want to delete: ")
    deletename=deletename.lower()
    contacts.pop(deletename)

def lookup_contact(contacts):
    '''Prompts the user for a contact name
       to view, then displays the email
       address stored for that contact in 
       the provided contacts dictionary.'''
    # Replace the line below with your code
    # to view a contact in the dictionary
    # passed into the function
    print('Look up contact')
    lookname = input("Enter the name of contact that you want to search: ")
    lookname=lookname.lower()
    print("The email address of "+lookname+" is "+contacts[lookname])
    
def main():
    '''Primary logic for the program'''
    # Contacts are stored in a pickle file
    # named contacts.p...or not, if no
    # contacts have yet been created
    #
    # Enter the full path to the contacts.p
    # file below, ending in a / character
    file_path = '/Users/Vivek/Desktop/Python NEC/'
    file_name = 'contacts.p'
    file_name = file_path + file_name
    try:
        # If file exists, fill contacts
        # dictionary with its contents
        f = open(file_name, 'rb')
        contacts = pickle.load(f)
        f.close()
    except:
        # If file not found, create an
        # empty contacts dictionary
        print('Whoops!')
        contacts = dict()
    # Now we're ready to call the menu
    # and get this program underway
    choice = run_menu()
    while choice != 'q':
        if choice == 'a':
            add_contact(contacts)
        elif choice == 'e':
            edit_contact(contacts)
        elif choice == 'd':
            delete_contact(contacts)
        else:
            lookup_contact(contacts)
            
        choice = run_menu()
    # The user pressed 'q'
    # Save updated contacts back to 
    # the pickle file and exit
    f = open(file_name, 'wb')
    pickle.dump(contacts, f)
    f.close()
    print('Contacts file saved...bye!')

if __name__=='__main__':
    main()