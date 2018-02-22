
# This is a program for a function tutorial


# Function 1
def LargestElement (arg_list):      # list is the variable name used in the function and = to arg1
    largestElement = 0
    for i in arg_list:
        if i > largestElement:
            largestElement = i
    return largestElement

def ReverseList(arg_list):
    rlist = []          # Define a blank new list
    for i in arg_list:  # for each value in arg_list run the loop
        rlist.insert(0, i)   # Adds each value in the list at the first position thus reversing the list
    return rlist        # When the function is called it sends the given list reversed
                        # list.reverse is already a function so shouldn't be used inside a function

# Main Body code

# Creates a list and continually asks for input until a blank is entered.
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
        print("The current values are: ")
        print(list)

if numberFlag:  # If the list contains numbers
    valueToPrint = LargestElement(list)
    print('The largest value entered is', valueToPrint)

listToPrint = ReverseList(list)
print('The list reversed is', ReverseList(list))