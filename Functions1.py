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
    i = 1           # Creates a counter
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
print('The list in its default state is: {0}'.format(list))

# Function 1 printing   only runs if list is only ints or floats
if numberFlag:  # If the list contains numbers
    valueToPrint = Function1ReturnLargest(list)     # Calling the function
    print('The largest value entered is', valueToPrint)     # Print the value returned from the function

# Function 2 printing
listToPrint = Function2Reverse(list)        # Calling the function
print('The list reversed is', listToPrint)  # Print the value returned from the function

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

# Function 4 printing
listToPrint = Function4ReturnsElementsInOddPositions(list)
print('The values in the list at odd positions are', listToPrint)

# Function 5 printing
if numberFlag:
    valueToPrint = Function5RunningTotal(list)
    print('The total of all the elements in the list is', valueToPrint)

# Function 6 printing
booleanToPrint = Function6PalindromeTest(list)
if booleanToPrint:
    print(list, 'is a palindrome.')
else:
    print(list, 'is not a palindrome')

# Function 7 printing
if numberFlag:
    valueToPrint = Function7SumNumbersForLoop(list)
    print('The sum of the list is', valueToPrint)
