''' Author: Ethan Cornish
Last Modified:  9/3/2018
Version:    1.0

The code stores a list of contacts that each contain a first name, last name, and date of birth.
The user can add, delete, change or search for a contact

The main list, contactsList is a list of list of lists. The first sub list is contains the names and date as a list.
The second sub list contains the individul names and individual dates.
'''


# John,Smith,01/01/2000
# Ed,White,05/11/1999
# Erin,Kirk,23/07/2994


# Loads contacts from a file called contacts.txt
# r_contactsList is the read contact list and will be returned
# r_contacts list is in the form of contactsList
def LoadContact():
    # Define the list and opening the file
    r_contactsList = []
    f = open('Module3PracticeTextfile', 'r')
    for line in f:
        # Defining a sub list to store names
        name = []
        # Formatting the line in the file before appending
        line = line.strip('\n')
        line = line.split(",")
        # Adding the first and last name to the names list as separate entries
        name.append(line[0])
        name.append(line[1])
        # Creating a second sub list to stor the date.
        date = line[2].split("/")
        # Adding the sub list to the main list in a single index value
        r_contactsList.append([name, date])
    f.close()
    # Outputting the main list
    return r_contactsList


# Searches through all of the names in the main list to find a specific name and return the index value
# searchName is the name the program is trying to find
# r_contactsList is the main list which is being read
def SearchFunction(searchName, r_contactsList):
    # Define a counting variable to store the index value and to be outputted
    position = 0
    for contact in r_contactsList:  # This runs through each set of name and date in the main list
        for name in contact[0]:     # contact[0] is the sub list containing first and last names
            if name == searchName:
                return position
        position += 1
    position = -1
    # If the name is not found then return -1
    return position


# Gets the details of a new contact and adds it to the list
# c_contactList is the main list that will be appended and then outputted
# SaveFile is a function run inside this function that updates the file containing the contacts
def NewContact(c_contactList):
    print("Enter the new contacts details")
    fname = input("Firstname: ")
    sname = input("Surname: ")
    print("Birthday")
    ddate = input("Day: ")
    mdate = input("Month: ")
    ydate = input("Year: ")
    # Define a sub list for names, sub list for date and append each variable as seperate value
    name = []
    date = []
    name.append(fname)
    name.append(sname)
    date.append(ddate)
    date.append(mdate)
    date.append(ydate)
    # Add name and date sub lists to the main list
    c_contactList.append([name,date])
    SaveFile(c_contactList)
    return c_contactList

# Allows the user to modify the date in a contact
# r_contactsList is the main list that will be read and updated
def ChangeBirthday(r_contactsList):
    # Request the name of the contact wished to be updated
    print('What is the name of the contact you wish to change birthday for?')
    name = input()
    # Use the search function to find the index value of the contact
    namePos = SearchFunction(name, r_contactsList)
    # If the contact does not exist inform the user and end the function
    if namePos == -1:
        print('The name you entered does not exist\n')
        return
    else:
        # Get input for the new date
        print('Enter the following for the new birthday')
        ddate = input("Day: ")
        mdate = input("Month: ")
        ydate = input("Year: ")
        # Create a sublist and add the input as one index
        date = []
        date.append([ddate,mdate,ydate])
        # Make the new date = the date sublist in the contact index given by the SearchFunction
        r_contactsList[namePos][1] = date   # The list[index][index] syntax is used to search a list in list
        # Display the updated list
        print(r_contactsList)
    return


# Allows the user to remove a contact
# r_contactsList is the main list to be read and updated
def DeleteContact(r_contactsList):
    # Request the contact wished to be deleted
    print('What is the name of the contact you wish to delete?')
    name = input()
    # Use the search function to find the index value of the contact
    namePos = SearchFunction(name, r_contactsList)
    # If the contact does not exist inform the user and end the function
    if namePos == -1:
        print('The name you entered does not exist\n')
    else:
        # Pop the entire contact at the index given by the SearchFunction
        delete = r_contactsList.pop(namePos)
        # Display the deleted contact
        print('You have deleted', delete)
    return


def LookupBirthday(r_contactsList):
    print('What is the name of the contact you would like to have their birthday displayed for?')
    name = input()
    namePos = SearchFunction(name, r_contactsList)
    if namePos == -1:
        print('The name you entered does not exist\n')
    else:
        display = r_contactsList[namePos]
        print('The contact is', display)
    return

#Saves a contact list back to a file in a format readable by LoadContacts()
def SaveFile(w_contactsList):
    f = open('Module3PracticeTextfile', 'w')
    for entry in w_contactsList:
        names = entry[0]
        f.write(names[0])
        f.write(',')
        f.write(names[1])
        f.write(',')
        cDate = entry[1]
        f.write(cDate[0])
        f.write('/')
        f.write(cDate[1])
        f.write('/')
        f.write(cDate[2])
        f.write('\n')
    f.close()
    print("File saved")
    return 1


menuOption = 0
contactsList = LoadContact()
print(contactsList)


while True: # Will occur forever
    print('Please enter the number of the option you wish to select:')
    print('    1. Look up contact')
    print('    2. Add a new contact')
    print('    3. Change a birthday')
    print('    4. Delete a contact with a birthday')
    print('    5. Quit the program')
    menuOption = input('Selection: ')
    print('\n')

    if menuOption == '1':
        LookupBirthday(contactsList)
    elif menuOption == '2':
        NewContact(contactsList)
    elif menuOption == '3':
        ChangeBirthday(contactsList)
    elif menuOption == '4':
        DeleteContact(contactsList)
    elif menuOption == '5':
        SaveFile(contactsList)
        print('exit(1)')
        exit(1)
    else:
        print('Menu option entered does not exist\n')
        menuOption = 0
