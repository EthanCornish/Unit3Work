from tkinter import *

toFootConst = 3.28084
toMetreConst = 0.3048

def FootToMetres(feet):
    metres = feet * toMetreConst
    return metres


def MetresToFeet(metres):
    feet = metres * toFootConst
    return feet


class ConversionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Imperial <----> Metric converter")

        self.titleText = Label(master, text="Select if you want feet or text:")
        self.titleText.grid()

        self.radioSelect = IntVar()

        self.radioI = Radiobutton(master, text="Feet to Metres", variable=self.radioSelect, value=0)
        self.radioI.grid(row=1)

        self.radioM = Radiobutton(master, text="Metres to Feet", variable=self.radioSelect, value=1)
        self.radioM.grid(row=2)

        self.feetLabel = Label(master, text="Enter a value to convert:")
        self.feetLabel.grid(columnspan=2, row=3)

        self.distance = DoubleVar()
        self.entryValue = Entry(master, textvariable=self.distance)
        self.entryValue.grid(row=4, columnspan=2)

        self.resultLabel = Label(master, text="Result:")
        self.resultLabel.grid(row=5)

        self.result = DoubleVar()
        self.resultValue = Label(master, textvariable=self.result)
        self.result.set(0.0)
        self.resultValue.grid(row=5, column=1)

        self.calcButton = Button(master, text="Calculate", command=self.convert)
        self.calcButton.grid(row=6)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=6, column=1)

    def convert(self):
        distance = self.distance.get()

        if not(self.radioSelect.get()):
            result = FootToMetres(distance)
        elif self.radioSelect.get():
            result = MetresToFeet(distance)
        self.result.set(result)
        return

root = Tk()
gui = ConversionGUI(root)
root.mainloop()
