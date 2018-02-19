
# exit(2) = Function1 non numerical input

# First function. Works for decimals, exit(2) if the list contains strings
def function1ReturnLargest (list):
    try:
        for x in list:
            x = float(x)
    except ValueError:
        print('Non Numerical Input Entered')
        exit(1)
    list.sort(key=float)
    return list

def function2Reverse (list):
    list.reverse()

# Creates the list allowing the user to input as many values as they want.
list = []
UI = "\n"
while (UI != ""):
    UI = input("Enter a value for the list: ")
    if (UI != ""):
        list.append(UI)
print('The list in its default state is: {0}'.format(list))

# Prints the list in ascending order
# listAscending = [function1ReturnLargest(list)]
print('The list in ascending order is {0}.'.format(function1ReturnLargest(list)))


