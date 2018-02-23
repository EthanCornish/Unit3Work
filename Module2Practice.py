# exit(2) = could not get classification due to negative number

# Function to get the profit
def GetProfit (sell, cost, sale):
    profit = sell * (sale - cost)
    return profit

# Function to get the classification
def GetVintage (total):
    if total > 100:
        classification = 'Excellent'
    elif 100 >= total >= 40:
        classification = 'Good'
    elif 40 > total > 0:
        classification = 'Poor'
    else:
        exit(2)
    return classification

# Function to get the values contained in the file
def InputFile():
    fname = ('weekly-harvest (1).txt')  # Hard code the filename to be read
    f = open(fname, 'r')                # Open the file to read
    totalList = []                      # Define list TotalList
    vlist = []
    for line in f:          # For each line in the file
        line = line.strip('\n')
        line = line.split(' ')      # Puts each line into a list seperated by a space

        vname = line.pop(0)
        vlist.append(vname)

        total = 0
        for i in line:      # for each element in in the line
#            print(line)
            grapeHarvest = i
#            total += grapeHarvest
            totalList.append(grapeHarvest)
        print(totalList)
    print(vlist)
    print(totalList)
    return totalList

# takes costPrice and salePrice input
#costPrice = input('What is the cost price per tonne. As a numerical value without units.')
#salePrice = input('What is the sale price per tonne. As a numerical value without units.')

# defines a list containing each vinyard
#vineyard = ['Chandra', 'Krishna', 'Vengi', 'Navneet', 'Sanjay', 'Amit', 'Masaba'
totalList = InputFile()
#    print(totalList)        # For testing, should contain each value in a single line without string
#print(vineyard)             # For testing should be a list of lists
