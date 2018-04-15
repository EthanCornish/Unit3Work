from tkinter import Tk, Label, Button, Entry, Radiobutton, DoubleVar, IntVar, StringVar

# exit 1 = invalid BMI
# exit 2 = invalid unit input
# exit 3 = invalid input (under metric)
# exit 4 = invalid input (under imperial)


# NOTE: Variables are set to float when being defined or re defined to allow algorithms to work.

# Start Functions

# Function for converting an imperial height to meters
def convertHeight(feet, inches):
    height = float((((feet * 12) + (inches)) * 0.0254))
    return height

# Function for converting an imperial weight to kgs
def convertWeight(lbs):
    weight = float((lbs * 0.45359237))
    return weight

# Function for for determining wat category the BMI lies in, underweight, Healthy Weight, Overweight
def getBMIcategory(BMI):
    if BMI >= 0 and BMI < 18.5:
        category = 'Underweight'
    elif BMI >= 18.5 and BMI < 25:
        category = 'Healthy Weight'
    elif BMI >= 250 and BMI < 30:
        category = 'Overweight'
    elif BMI >= 30:
        category = 'Obese'
    # If the BMI is negative or greater than 30 it ends the program
    else:
        print('Invalid input entered')
        exit(1)
    return category


# Start main code
def main():
    # Used to test the unit input
    unitGood = False

    # Getting input for height, weight and unit. Unit is asked first as it is used to determine whether to ask for
    # height in meters or in feet and inches.
    # Try blocks used to detect non numberical input for height, weight, feet, inches
    units = input('Would you like to enter your information in metric or imperial')
        # Uses unitGood variable and a while and if loop to check if the unit input is valid, if not exit(2)
    while unitGood == False:
        if units == 'Metric' or units == 'metric' or units == 'Imperial' or units == 'imperial':
            unitGood = True
        else:
            print('Invalid Input')
            exit(2)

    if units == 'Metric' or units == 'metric':
        height = input('What is your height in meters?')
        try:
            height = float(height)
        except ValueError:
            print('Invalid Input')
            exit(3)
        weight = input('What is your weight in kgs?')
        try:
            weight = float(weight)
        except ValueError:
            print('Invalid Input')
            exit(3)
    if units == 'Imperial' or units == 'imperial':
        # Tells the user how the program will ask for feet and inches separately. This is done so the height can be
        # calculated correctly
        print('The program will ask for your how many feet you are then inches separately.')
        feet = float(input('What is your height in feet?'))
        try:
            feet = float(feet)
        except ValueError:
            print('Invalid Input')
            exit(4)
        inches = float(input('What is your height in inches?'))
        try:
            inches = float(inches)
        except ValueError:
            print('Invalid Input')
            exit(4)
        weight = float(input('What is your weight in lbs?'))
        try:
            weight = float(weight)
        except ValueError:
            print('Invalid Input')
            exit(4)

    # if the units given are imperial it uses the functions 'convertHeight' and 'convertWeight' from the beginning...
    # of the file to calculate the heightInMeters and weightInKgs respectively
    if units == 'Imperial' or units == 'imperial':
        heightInMetres = convertHeight(feet, inches)
        weightInKgs = float(convertWeight(weight))
    # if the units given aren't imperial then converts them from height to heightinMeters and weight to weightInKgs as...
    # they are
    else:
        heightInMetres = height
        weightInKgs = weight

    # Converts both heightInMeters and weightInKgs to floats to allow the algorithm to work correctly
    heightInMetres = float(heightInMetres)
    weightInKgs = float(weightInKgs)

    # Calculates the bmi as a float
    bmi = float(weightInKgs/(heightInMetres*heightInMetres))
    # Calls the getBMIcategory function from the start of the file to determine the category
    category = getBMIcategory(bmi)
    # Outputs the BMI and the category
    print('Your BMI is {0:.2f} which gives you a category of {1}'.format(bmi, category))

# main()

class GUICreation:

    def __init__(self, master):
        self.master = master
        master.title('A BMI Calculator')

        # Title
        self.titleLabel = Label(master, text='A BMI Calculator')
        self.titleLabel.grid(row=0, column=0, columnspan=2)

        # Radio Buttons for choosing unit
        self.unit = IntVar()
        self.radioMetric = Radiobutton(master, text='Metric', variable=self.unit, value=0)
        self.radioMetric.grid(row=1, column=0)
        self.radioImperial = Radiobutton(master, text='Imperial', variable=self.unit, value=1)
        self.radioImperial.grid(row=1, column=1)

        # Input (height)
        if not (self.unit.get()):
            self.inputHeight = DoubleVar()
            self.inputHeightLabel = Label(master, text='What is your height in meters: ')
            self.inputHeightEntry = Entry(master, textvariable=self.inputHeight)

            self.inputHeightLabel.grid(row=3, column=0)
            self.inputHeightEntry.grid(row=3, column=1)

        elif self.unit.get:
            self.inputHeightFeet = IntVar()
            self.inputHeightInch = IntVar()
            self.inputHeightLabel = Label(master, text='What is your height in;')
            self.inputHeightLabelFeet = Label(master, text='Feet: ')
            self.inputHeightLabelInch = Label(master, text='Inches: ')
            self.inputHeightEntryFeet = Entry(master, textvariable=self.inputHeightFeet)
            self.inputHeightEntryInch = Entry(master, textvariable=self.inputHeightInch)

            self.inputHeightLabel.grid(row=3, column=0, columnspan=4)
            self.inputHeightLabelFeet.grid(row=3, column=1)
            self.inputHeightEntryFeet.grid(row=3, column=2)
            self.inputHeightLabelInch.grid(row=3, column=3)
            self.inputHeightEntryInch.grid(row=3, column=4)

root = Tk()
GUI = GUICreation(root)
root.mainloop()