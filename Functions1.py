import copy     # Used in Function 5

# from FunctionsTutorial import LargestElement          syntax to import functions from other files
# x = LargestElement(list)                              x = return value from function

# Function 1. Returns largest element
def Function1ReturnLargest (list):
    largestElement = 0      # Defining largest element
    for i in list:          # For each element in the list
        if i > largestElement:  # If the element being checked is greater than the largest element
            largestElement = i  # Largest element = the element
    return largestElement

# Function 2. Reverses the list
def Function2Reverse (list):
    rlist = []  # Define a blank new list which will contain list but reversed
    for i in list:  # for each value in the list
        rlist.insert(0, i)  # Adds each value in the list at the first position thus reversing the list
    return rlist  # When the function is called it sends the given list reversed
    # list.reverse is already a function so shouldn't be used inside a function

# Function 3. Checks if the an element is in the list
def Function3ElementExistCheck (list, valueWanted):
    elementExist = False        # Creates a flag to check if an element in the list is wanted
    for i in list:         # For each element in the list while elementExist = false
        if valueWanted == i:                  # If the value wanted equal the element in the list elementExist = True
            elementExist = True
    return elementExist                        # Returns the bullion

# Function 4. Returns elements in an odd position
def Function4ReturnsElementsInOddPositions (list):
    dlist = []
    dlist = copy.copy(list)   # Creates a duplicate list that can be popped
    olist = []      # Creates a new list to store the values at odd positions
    i = 0           # Creates a counter
    while i < len(dlist):        # While the counter is less than the length of the list
        olist.append(dlist.pop(i))       # Add the value in the position of i in the list to the new list
        i += 1                          # Add 1 to the counter
    return olist

# Function 5. Returns the running total of the list
def Function5RunningTotal (list):
    rTotal = 0          # Creates a variable to store the running total
    for i in list:      # For each element in the list
        rTotal += i         # Running total = the running total plus the element in the list
    return rTotal

# Function 6. Tests if a list is a palindrome
def Function6PalindromeTest (list):
    relist = Function2Reverse(list)
    if list == relist:
        return True
    return False

# Function 7a. Sum of numbers in a list using for loop
def Function7SumNumbersForLoop (list):
    try:
        sum = list.pop()
    except IndexError:
        return 0
    return sum + Function7SumNumbersForLoop(list)


# Main Code

# Creates the list allowing the user to input as many values as they want.
list = []   # Define a list
UI = "\n"
numberFlag = True   # A flag to check if a list contains only numbers
while (UI != ""):
    UI = input("Enter a value for the list: ")
    if (UI != ""):
        # Checks if value entered can be a float
        try:
            UI = float(UI)
        except ValueError:
            numberFlag = False
        list.append(UI)
print('The list in its default state is: {0}\n'.format(list))

print('The program can perform a variety of manipulations on the function.\n')
print('Enter the corresponding number to run a specific option.\n')
print('1 = Return the largest value.\n2 = Reverse the list.\n3 = Check if a specific value is in the list.')
print('4 = Return the values in odd positions in the list\n5 = To print a total of the list.')
print('6 = Return if the list is a palindrome.\n7 = Print the sum of the list using a recursion method.')
print('0 = Exit the program.')
print('––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––\n\n\n')
run = input()
try:
    run = int(run)
except ValueError:
    print('You did not enter valid input')
    exit(2)

while run != 0:
    if run == 1:
        # Function 1 printing   only runs if list is only ints or floats
        if numberFlag:  # If the list contains numbers
            valueToPrint = Function1ReturnLargest(list)  # Calling the function
            print('The largest value entered is', valueToPrint)  # Print the value returned from the function
    elif run == 2:
        # Function 2 printing
        listToPrint = Function2Reverse(list)  # Calling the function
        print('The list reversed is', listToPrint)  # Print the value returned from the function
    elif run == 3:
        # Function 3 printing
        element = (input('What element would you like to check if it is in the list?'))
        try:
            element = float(element)
            run3 = True
        except ValueError:
            print('The element you entered is not a number.')
        if numberFlag:
            elementToPrint = Function3ElementExistCheck(list, element)
            if elementToPrint:
                print(element, 'is in the list.')
            else:
                print(element, 'is not in the list')
    elif run == 4:
        # Function 4 printing
        listToPrint = Function4ReturnsElementsInOddPositions(list)
        print('The values in the list at odd positions are', listToPrint)
    elif run == 5:
        # Function 5 printing
        if numberFlag:
            valueToPrint = Function5RunningTotal(list)
            print('The total of all the elements in the list is', valueToPrint)
    elif run == 6:
        # Function 6 printing
        booleanToPrint = Function6PalindromeTest(list)
        if booleanToPrint:
            print(list, 'is a palindrome.')
        else:
            print(list, 'is not a palindrome')
    elif run == 7:
        # Function 7 printing
        if numberFlag:
            valueToPrint = Function7SumNumbersForLoop(list)
            print('The sum of the list is', valueToPrint)
    elif run == 0:
        print('You have chosen to end the program.')
        exit(1)
    else:
        print('Please enter a number ranging from 0-7 inclusive.')
        run = input()
    print('If you would like to operate further on your list enter another corresponding the input.')
    print('If you would like to end the program enter 0')
    run = int(input())

