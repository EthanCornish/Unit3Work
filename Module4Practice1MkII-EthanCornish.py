from tkinter import *

# FUNCTION for calculating BAC
def calcBAC(A, r, W, t):
    # Error doing algorithm unless float cast first
    A = float(A)
    r = float(r)
    W = float(W)
    t = float(t)
    ans = A/(r*W)*100 - (0.00015*t)
    return ans


def classification(status, BAC):
    if status == 0:
        if BAC > 0:
            result = 'License cancelled, interlock device'
            return result
        else:
            result = 'Safe to Drive'
            return result
    if status == 1:
        if BAC > 0.07:
            result = 'License cancelled, interlock device'
            return result
        elif 0.07 > BAC > 0.05:
            result = 'Fine and 10 demerit points'
            return result
        else:
            result = 'OK to Drive'
            return result


class BACcalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title('BAC Calculator')

        self.title = Label(master, text='This program will estimate your BAC (blood alchol concentration)')
        self.title.grid(column=0,row=0,columnspan=3,sticky=W)

        self.variableGenderSelection = IntVar()
        self.labelGender = Label(master, text='Gender:')
        self.radioGenderM = Radiobutton(master, text='Male', variable=self.variableGenderSelection, value=0)
        self.radioGenderF = Radiobutton(master, text='Female', variable=self.variableGenderSelection, value=1)
        self.labelGender.grid(column=0,row=1,columnspan=2,sticky=W)
        self.radioGenderM.grid(column=1,row=1,sticky=W)
        self.radioGenderF.grid(column=2,row=1,sticky=W)

        self.variableMassValue = DoubleVar()
        self.labelMass = Label(master, text='Mass as a number in Kg or lb:')
        self.entryMass = Entry(master, textvariable=self.variableMassValue)
        self.labelMass.grid(column=0,row=2,columnspan=2,sticky=W)
        self.entryMass.grid(column=2,row=2,sticky=W)

        self.variableUnitSelection = IntVar()
        self.labelUnit = Label(master, text='Unit used:')
        self.radioUnitKg = Radiobutton(master, text='Kg', variable=self.variableUnitSelection, value = 0)
        self.radioUnitlb = Radiobutton(master, text='lb', variable=self.variableUnitSelection, value = 1)
        self.labelUnit.grid(column=0,row=3,sticky=W)
        self.radioUnitKg.grid(column=1,row=3,sticky=W)
        self.radioUnitlb.grid(column=2,row=3,sticky=W)

        self.variableTime = DoubleVar()
        self.labelTime = Label(master, text='Time (hours):')
        self.entryTime = Entry(master, textvariable=self.variableTime)
        self.labelTime.grid(column=0,row=4,sticky=W)
        self.entryTime.grid(column=1,row=4,sticky=W)

        self.variableDrinks = DoubleVar()
        self.labelDrinks = Label(master, text='Drinks (standard):')
        self.entryDrinks = Entry(master, textvariable=self.variableDrinks)
        self.labelDrinks.grid(column=0, row=5,sticky=W)
        self.entryDrinks.grid(column=1,row=5,sticky=W)

        self.variableStatus = IntVar()
        self.labelStatus = Label(master, text='Current Licence Held:')
        self.radioStatusL = Radiobutton(master, text='Learners', variable=self.variableStatus, value=0)
        self.radioStatusP = Radiobutton(master, text='Probationary', variable=self.variableStatus, value=1)
        self.radioStatusFL = Radiobutton(master, text='Full License', variable=self.variableStatus, value=2)
        self.labelStatus.grid(column=0,row=6,columnspan=3,sticky=W)
        self.radioStatusL.grid(column=0,row=7,sticky=W)
        self.radioStatusP.grid(column=1,row=7,sticky=W)
        self.radioStatusFL.grid(column=2,row=7,sticky=W)

        self.variableOutputBAC = DoubleVar()
        self.variableOutputText = StringVar()
        self.labelOutputLabel = Label(master, text='You BAC is:')
        self.labelOutputBAC = Label(master, textvariable=self.variableOutputBAC)
        self.labelOutputText = Label(master, textvariable=self.variableOutputText)
        self.labelOutputLabel.grid(column=0,row=8,sticky=W)
        self.labelOutputBAC.grid(column=1,row=8,sticky=W)
        self.labelOutputText.grid(column=2,row=8,sticky=W)

        self.buttonCalculate = Button(master, text='Calculate BAC', command=self.calc)
        self.buttonClose = Button(master, text='Close', command=master.quit)
        self.buttonCalculate.grid(column=0, row=9,sticky=W)
        self.buttonClose.grid(column=2,row=9,sticky=W)

    def calc(self):
        gender = self.variableGenderSelection.get()
        mass = self.variableMassValue.get()
        unit = self.variableUnitSelection.get()
        time = self.variableTime.get()
        drinks = self.variableDrinks.get()
        status = self.variableStatus.get()

        if unit == 0:
            W = mass * 1000
        elif unit == 1:
            W = mass * 453.592
        else:
            print('Error with mass and units')
            exit(0)

        if gender == 0:
            r = 0.68
        elif gender == 1:
             r = 0.55
        else:
            print('Error with gender')

        A = drinks * 10

        BAC = calcBAC(A, r, W, time)
        consequence = classification(status, BAC)

        self.variableOutputBAC.set('{0:.2f}'.format(BAC))
        self.variableOutputText.set(consequence)
        return


root = Tk()
gui = BACcalculatorGUI(root)
root.mainloop()
