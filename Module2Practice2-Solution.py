#Exit code 1 = invalid units
#Exit code 2 = invalid gender
#Exit code 3 = invalid lincence entered
#Exit code 4 = none number mass
#Exit code 5 = none number time
#Exit code 6 = none number drinks

from tkinter import *

#FUNCTION for calculating BAC
def calcBAC(A, r, W, t):
    #Error doing algorithm unless float cast first
    A = float(A)
    r = float(r)
    W = float(W)
    t = float(t)
    ans = A/(r*W)*100 -(0.00015*t)
    return ans


# Start of Main program for CLI
# Taking input from users for: gender, mass, status, time, drinks, units
# Try blocks to detect invalid input for number values
def CLI():
    gender = input("What gender are you (m/f): ")
    mass = input("Mass as number (Kg or lb):")
    try:
        mass = float(mass)
    except ValueError:
        print("None number input for mass")
        exit(4)
    status = input("Status (FL/P/L): ")
    time = input("Time (hours): ")
    try:
        time = float(time)
    except ValueError:
        print("None number input for time")
        exit(5)
    drinks = input("Drinks (standard): ")
    try:
        drinks = float(drinks)
    except ValueError:
        print("None number input for drinks")
        exit(6)
    units = input("Units (Kg or lb): ")
    W = MassConv(units, mass)
    r = GenderConstant(gender)
    # Calulate A based on standard drinks entered
    A = drinks * 10
    # BAC calulated by calcBAC function from start of this file
    BAC = calcBAC(A, r, W, time)
    BAC = round(BAC, 4)
    # Print out the BAC for the user to see and for debugging
    print("Estimated BAC is ", BAC)
    print(LicenceCheck(status, BAC))


# Converting entered mass value to Grams
def MassConv(units, mass):
    if(units == "Kg"):
        W = mass * 1000
    elif(units == "lb"):
        W = mass * 453.592
    else:
        print("Invalid units entered")
        exit(1)
    return W


# Determining conversion factor based on gender entered
def GenderConstant(gender):
    if(gender == "m" or gender == "M"):
        r = 0.68
    elif(gender == "f" or gender == "F"):
        r = 0.55
    else:
        print("Unrecognised gender entered")
        exit(2)
    return r



def LicenceCheck(status, BAC):
    #Inform the user if they are on an L or P licence what will happen if they drive
    if(status == "L" or status == "P"):
        if(BAC > 0):
            return "License cancelled, interlock device"
        else:
            return "Safe to drive"

    #Inform the user if they are on an FL licence what will happen if they drive
    if(status == "FL"):
        if(BAC > 0.07):
            return "License cancelled, interlock device"
        elif(BAC >0.05 and BAC<0.07):
            return "Fine and 10 demerit points"
        else:
            return "OK to drive"

class BACGUI:
    def __init__(self, master):
        self.master = master
        master.title("BAC calculator")

        self.titleText = Label(master, text="------------\nBAC CALCULATOR\n------------")
        self.titleText.grid()

        self.genderLabel = Label(master, text="Select your gender:")
        self.genderLabel.grid()

        self.radioSelectG = StringVar()

        self.radiom = Radiobutton(master, text="Male", variable=self.radioSelectG, value="M")
        self.radiom.grid(sticky="W")
        self.radiom.select()

        self.radiof = Radiobutton(master, text="Female", variable=self.radioSelectG, value="F")
        self.radiof.grid(sticky="W")

        self.unitLabel = Label(master, text="Select Units and enter your Weight:")
        self.unitLabel.grid()

        self.radioSelectU = StringVar()

        self.radiomet = Radiobutton(master, text="Kg", variable=self.radioSelectU, value="Kg")
        self.radiomet.grid(sticky="W")
        self.radiomet.select()

        self.radioimp = Radiobutton(master, text="lbs", variable=self.radioSelectU, value="lb")
        self.radioimp.grid(sticky="W")

        self.weight = DoubleVar()
        self.entryValue = Entry(master, textvariable=self.weight)
        self.weight.set(60)
        self.entryValue.grid()

        self.licenceLabel = Label(master, text="Select your Licence:")
        self.licenceLabel.grid()

        self.radioSelectL = StringVar()

        self.radiofl = Radiobutton(master, text="Full Licence", variable=self.radioSelectL, value="FL")
        self.radiofl.grid(sticky="W")
        self.radiofl.select()

        self.radiop = Radiobutton(master, text="Probationary Licence", variable=self.radioSelectL, value="P")
        self.radiop.grid(sticky="W")

        self.radiol = Radiobutton(master, text="Learner Licence", variable=self.radioSelectL, value="L")
        self.radiol.grid(sticky="W")

        self.drinksLabel = Label(master, text="Enter your number of standard drinks:")
        self.drinksLabel.grid()

        self.drinks = DoubleVar()
        self.entryDrinkValue = Entry(master, textvariable=self.drinks)
        self.drinks.set(1)
        self.entryDrinkValue.grid()

        self.timeLabel = Label(master, text="Enter how many hours since you started drinking:")
        self.timeLabel.grid()

        self.time = IntVar()
        self.entrytimeValue = Entry(master, textvariable=self.time)
        self.time.set(1)
        self.entrytimeValue.grid()

        self.spacer0 = Label(master, text="------------")
        self.spacer0.grid()

        self.resultLabel = Label(master, text="Result:")
        self.resultLabel.grid()

        self.result = DoubleVar()
        self.resultValue = Label(master, textvariable=self.result)
        self.resultValue.grid()

        self.BAC = DoubleVar()
        self.BACValue = Label(master, textvariable=self.BAC)
        self.BACValue.grid()

        self.spacer1 = Label(master, text="------------")
        self.spacer1.grid()

        self.calcButton = Button(master, text="Calculate", command=self.mainBACcalc)
        self.calcButton.grid()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid()

    def mainBACcalc(self):
        units = self.radioSelectU.get()
        gender = self.radioSelectG.get()
        time = self.time.get()
        mass = self.weight.get()
        status = self.radioSelectL.get()
        drinks = self.drinks.get()

        W = MassConv(units, mass)
        r = GenderConstant(gender)
        A = drinks * 10
        BAC = calcBAC(A, r, W, time)
        BAC = round(BAC, 4)
        result = LicenceCheck(status, BAC)
        self.result.set(result)
        self.BAC.set(BAC)
        return

root = Tk()
gui = BACGUI(root)
root.mainloop()