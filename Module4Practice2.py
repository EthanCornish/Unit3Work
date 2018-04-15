from tkinter import *

# Exit code 1 = invalid units
# Exit code 2 = invalid gender
# Exit code 3 = invalid licence entered
# Exit code 4 = none number mass
# Exit code 5 = none number time
# Exit code 6 = none number drinks


# FUNCTION for calculating BAC
def algorithm(A, r, W, t):
    # Error doing algorithm unless float cast first
    A = float(A)
    r = float(r)
    W = float(W)
    t = float(t)
    ans = A/(r*W)*100 -(0.00015*t)
    return ans



class GUI:
    def __init__(self, master):
        self.master = master
        master.title('A BAC Calculator')

        # Title Label
        self.titleLabel = Label(master, text='A Blood Alcohol Content (BAC) Estimator')
        self.titleLabel.grid(row=0,column=0,columnspan=3)

        # Getting Gender Input
        self.variableGender = StringVar()
        self.labelGender = Label(master, text='Gender: ')
        self.radioGenderM = Radiobutton(master, text='Male', variable=self.variableGender, value='M')
        self.radioGenderF = Radiobutton(master, text='Female', variable=self.variableGender, value='F')
        self.labelGender.grid(row=1,column=0)
        self.radioGenderM.grid(row=1,column=1)
        self.radioGenderF.grid(row=1,column=2)

        # Getting Mass input
        self.variableMass = DoubleVar()
        self.labelMass = Label(master, text='What is your mass (as a number, Kg or lb): ')
        self.entryMass = Entry(master, textvariable=self.variableMass)
        self.labelMass.grid(row=2,column=0,columnspan=2)
        self.entryMass.grid(row=2,column=2)

        # Getting Unit input
        self.variableUnit = StringVar()
        self.labelUnit = Label(master, text='Which unit did you use: ')
        self.radioUnitKg = Radiobutton(master, text='Kg', variable=self.variableUnit, value = 'Kg')
        self.radioUnitLb = Radiobutton(master, text='lb', variable=self.variableUnit, value = 'lb')
        self.labelUnit.grid(row=3,column=0)
        self.radioUnitKg.grid(row=3,column=1)
        self.radioUnitLb.grid(row=3,column=2)

        # Getting Status input
        self.variableStatus = StringVar()
        self.labelStatus = Label(master, text='Which license do you possess: ')
        self.radioStatusL = Radiobutton(master, text='Learners', textvariable=self.variableStatus, value='L')
        self.radioStatusP = Radiobutton(master, text='Probationary', textvariable=self.variableStatus, value='P')
        self.radioStatusFL = Radiobutton(master, text='Full License', textvariable=self.variableStatus, value='FL')
        self.labelStatus.grid(row=4,column=0)
        self.radioStatusL.grid(row=4,column=1)
        self.radioStatusP.grid(row=4,column=2)
        self.radioStatusFL.grid(row=4,column=3)

        # Getting Time input
        self.variableTime = DoubleVar()
        self.labelTime = Label(master, text='Number of hours since last drink: ')
        self.entryTime = Entry(master, textvariable=self.variableTime)
        self.labelTime.grid(row=5,column=0,columnspan=3)
        self.entryTime.grid(row=5,column=4)

        # Getting Drinks input
        self.variableDrinks = DoubleVar()
        self.labelDrinks = Label(master, text='Number of standard drinks consumed: ')
        self.entryDrinks = Entry(master, textvariable=self.variableDrinks)
        self.labelDrinks.grid(row=6,column=0, columnspan=3)
        self.entryDrinks.grid(row=6,column=3)

        # Output
        self.variableOutputNo = DoubleVar()
        self.variableOutputTxt = StringVar()
        self.labelOutput = Label(master, text='Your Estimated BAC is: ')
        self.labelOutputNo = Label(master, textvariable=self.variableOutputNo)
        self.labelOutputTxt = Label(master, textvariable=self.variableOutputTxt)
        self.labelOutput.grid(row=7, column=0, columnspan=3)
        self.labelOutputNo.grid(row=7, column=3)
        self.labelOutputTxt.grid(row=8, column=0)

        # Buttons for calculate and close
        self.buttonCalc = Button(master, text='Calculate', command=self.calculate)
        self.buttonClose = Button(master, text='Close', command=master.quit)
        self.buttonCalc.grid(row=9,column=0)
        self.buttonClose.grid(row=9,column=3)

    # Function to Calculate BAC
    def calculate (self):
        gender = self.variableGender.get()
        mass = self.variableMass.get()
        status = self.variableStatus.get()
        time = self.variableTime.get()
        drinks = self.variableDrinks.get()
        unit = self.variableUnit.get()

        if unit == 'Kg':
            W = mass * 1000

        elif unit == "lb":
            W = mass * 453.592

        if gender == "M":
            r = 0.68
        elif gender == "F":
            r = 0.55

        A = drinks * 10

        BAC = algorithm(A, r, W, time)
        self.variableOutputNo.set(BAC)

        if status == 'L' or status == 'P':
            if (BAC > 0):
                self.variableOutputTxt.set('License cancelled, interlock device')
                exit(0)
            else:
                self.variableOutputTxt.set('Safe to Drive')

        if status == 'FL':
            if BAC > 0.0:
                self.variableOutputTxt.set('License cancelled, interlock device')
            elif BAC > 0.05 and BAC < 0.07:
                self.variableOutputTxt.set('Fine and 10 demerit points')
            else:
                self.variableOutputTxt.set('OK to drive')
        print(BAC)
        print(self.variableOutputNo)
        print(self.variableOutputTxt)


root = Tk()
my_gui = GUI(root)
root.mainloop()
