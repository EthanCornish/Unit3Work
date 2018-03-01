# exit(2) = could not get classification due to negative number


# Function to get the profit
def GetProfit(sell, cost, sale):
    profit = sell * (sale - cost)
    return profit


# Function to get the classification
def GetVintage(total):
    if total > 100:
        classification = 'Excellent'
    elif 100 >= total >= 40:
        classification = 'Good'
    elif 40 > total > 0:
        classification = 'Poor'
    else:
        exit(2)
    return classification


# Function to get the lowest value in total list
def ReturnSmallest (list):
    smallestElement = 100
    for i in list:
        if i < smallestElement:
            smallestElement = i
    return smallestElement


def ReturnLargest (list):
    largestElement = 0
    for i in list:
        if i > largestElement:
            largestElement = i
    return largestElement


# takes costPrice and salePrice input
costPrice = float(input('What is the cost price per tonne. As a numerical value without units.'))
salePrice = float(input('What is the sale price per tonne. As a numerical value without units.'))

fname = ('weekly-harvest (1).txt')  # Hard code the filename to be read
f = open(fname, 'r')                # Open the file to read
totalList = []                      # Define list TotalList
vlist = []
grapeHarvest = []

for line in f:          # For each line in the file
    line = line.strip('\n')
    line = line.split(' ')      # Puts each line into a list separated by a space
    vname = line.pop(0)         # Stores the name of the vineyard in a variable
    vlist.append(vname)         # Puts the name of each vineyard in a list
    total = 0
    for i in line:              # For each value in the line
        total += float(i)       # Add the variable to a running total
    totalList.append(total)     # Add the running total to totalList the
f.close()

totalGrapes = 0
for value in totalList:         # For each value in totalList
    totalGrapes = value + totalGrapes   # Add to a running total variable that will contain the full total number

print('vlist =', vlist)
print('totalList =', totalList)
print('totalGrapes = {0:.2f}'.format(totalGrapes))

average = totalGrapes / len(vlist)      # Average the number of grapes across each vineyard.

lowest = ReturnSmallest(totalList)         # Gets the lowest number of grapes out of the vineyards with function
lowestIndex = totalList.index(lowest)    # Finds the index value of lowest, stores it a smallestIndex
lowestVineyard = vlist[lowestIndex]      # Uses smallestIndex to match lowest with its vineyard

highest = ReturnLargest(totalList)          # Repeats the process for highest
highestIndex = totalList.index(highest)
highestVineyard = vlist[highestIndex]
sellAmount = totalGrapes * (45/100)     # Calculates sell amount
profit = GetProfit(sellAmount, costPrice, salePrice)    # Calculates the profit using function
vintage = GetVintage(totalGrapes)   # Calculates category using function

output = ('\nThe total mass of the grapes harvested is {0:.2f}.\nThe average mass of grapes harvested is {1:.2f}.\nThe '
      'vineyard that produced the highest amount of grapes was {2} with {3} grapes.\nThe vineyard that produced the '
      'least amount of  grapes was {4} with {5} grapes.\nThere is an expected profit of ${6:.2f}\nThe vintage '
      'classification is {7}.'.format(totalGrapes, average, highestVineyard, highest, lowestVineyard, lowest,
                                      profit, vintage))
print(output)


f = open('Module2PracticeOutput', 'w+')
f.write(output)
