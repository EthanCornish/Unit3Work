''' Author: Ethan Cornish
Last Modified: 9/3/2018
Version 1.0 '''

# Module3Practice2Textfile.txt

# john 21 12 11 2 4 13
# Nick 12 3 8 15
# Steve 9 10

# Reads given file and writes each line to a list
# fname is a variable that store the name of the fle being used, it is global because it is needed in the SaveFunction
# mainList is the list that stores each line as a separate value
def LoadFunction():
    global fname
    fname = input('What is the name of the file you wish to work with?\n(This will be the file added to if you create a '
                  'new player and/or if you load previous data and/or if you Search & Display')
    file = open(fname, 'r')
    mainList = []
    for line in file:
        # Formatting the line in the file before appending
        line = line.strip('\n')
        line = line.split(',')
        mainList.append(line)
    file.close()
    return mainList


# Adds a new player to the list
# mainList is the list created in LoadFunction
# add is the new player
# SaveFunction is run in order to save the new player to the original file instantly
def NewData(mainList):
    print("Please enter the player's name and number of games seperated with spaces. Press enter when done. The name "
          "must be one word")
    add = input()
    mainList.append([add])
    SaveFunction(mainList)
    return

# Displays all other entries in the file
# list is the mainList from the other functions it is called list in this function for convenience
def LoadPrevious(list):
    for player in list:     # For each item in the list
        for i in player:
            print(i)       # Display the item
    return


# Takes a given name and searches through each value in the list until it is found
#   if found it runs PlayerAnalyse to give the output
#   if not found it tells the user and ends the function
# list is the mainList
# wantedPlayer stores the name of the player being searched for
def SearchPlayer(list):
    print('SearchPlayer')
    wantedPlayer = input('What is the player you wish to display statistics for?\n')
    position = 0    # Create a counter variable
    while position < len(list): # Check that the counter is smaller than the list
        for player in list: # For each item in the list
            strPlayer = ' '.join(player)    # Take the item and store it as a string
            playerList = strPlayer.split(' ')   # Take the string and place in a new list with each value its own index
            if playerList[0] == wantedPlayer:   # If the first value in the new list (the name) is the wantedPlayer
                PlayerAnalyse(playerList)       # Run PlayerAnalyse, give the new list as the arguement
                return
            position += 1
    print('The player name given was not found')    # If the wantedPlayer is not found then inform user
    return


# Called inside SearchPlayer and takes a list with a name followed by numerical values (scores) as separate indexes
# PlayerListS contains only the numerical values from playerList into a new list to allow for math
# gamesPlayed is the amount of numerical values in playerList
# totalScore is the sum of the numerical values in playerList
# ppg is the average of the numerical values in playerList
# max is the highest value
def PlayerAnalyse(playerList):
    if playerList[-1] == '':    # Checks if there is an extra space on the end of the list
      playerList.pop(-1)  # If there are then remove it, this is done now to prevent bugs when working with playerListS

    playerListS = playerList.copy()     # Creating playerListS without modifying playerList
    playerListS.pop(0)

    gamesPlayed = ((len(playerList)) - 1)

    totalScore = 0          # Define totalScore as a counting variable
    for i in playerListS:   # For each value
        i = int(i)          # Convert the value to an int (this stopped a bug)
        totalScore += i     # Add the value to totalScore

    ppg = totalScore / gamesPlayed

    max = 0
    for score in playerListS:
        score = int(score)
        if score > max:
            max = score

    maxIndex = 0
#    check = True
#    while check:
    for value in playerListS:
        if value != max:
            maxIndex += 1


    display = ("{0} had a total score of {1} points with an average of {2:.1f} points per game "
               "(ppg) over {3} games. {0}'s highest scoring game was {4} with {5} points".format(playerList[0],
                                                                        totalScore, ppg, gamesPlayed, maxIndex, max))
    print(display)
    return

def SaveFunction(list):
    file = open(fname, 'w')
    for entry in list:
        count = 0
        while count < len(entry):
            file.write(entry[count])
            file.write(' ')
            count += 1
        file.write('\n')
    file.close()
    return

mainList = LoadFunction()
menuOption = 0


while True:
    print('\nPlease enter the number of the option you wish to select:')
    print('     1: Enter new data')
    print('     2: Load Previous data')
    print('     3: Search for a player and display statistics')
    print('     4: Quit the program\n')
    menuOption = input()

    if menuOption == '1':
        NewData(mainList)
    elif menuOption == '2':
        LoadPrevious(mainList)
    elif menuOption == '3':
        SearchPlayer(mainList)
    elif menuOption == '4':
        print('You have chosen to exit the program.')
        exit(1)
    else:
        print('Menu option entered does not exist\n')
        menuOption = 0