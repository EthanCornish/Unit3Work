from tkinter import Tk, Label, Button, Entry, DoubleVar, IntVar, Radiobutton


class MetersToFeetGUI:

    def __init__(self, master):
        self.master = master
        master.title('A Meter to Feet Converter')

        # Title
        self.titleLabel = Label(master, text='A Meter to Feet Converter')

        # Radio Buttons
        self.mode = IntVar()
        self.radioMtoF = Radiobutton(master, text='Meter to Feet', variable=self.mode, value = 0)
        self.radioFtoM = Radiobutton(master, text='Feet to Meter', variable=self.mode, value = 1)

        # Input
        self.inputLabel = Label(master, text='Enter a number')
        self.input = DoubleVar()
        self.inputEntry = Entry(master, textvariable=self.input, width=8)

        # Output
        self.outputLabel = Label(master, text='Result:  ')
        self.output = DoubleVar()
        self.outputValue = Label(master, textvariable=self.output, width=10)

        # Buttons for calculate and close
        self.calcButton = Button(master, text = 'Calculate', command = self.convert)
        self.closeButton = Button(master, text='Close', command = master.quit)

        # Grid placements
        self.titleLabel.grid(row=0, column=0, columnspan=2)
        self.radioMtoF.grid(row=1, column=0)
        self.radioFtoM.grid(row=2, column=0)
        self.inputLabel.grid(row=3, column=0)
        self.inputEntry.grid(row=3, column=1)
        self.outputLabel.grid(row=4, column=0)
        self.outputValue.grid(row=4, column=1)
        self.calcButton.grid(row=5, column=0)
        self.closeButton.grid(row=5, column=1)

    def convert(self):
        input = self.input.get()
        conversion = self.mode.get()
        if conversion == 0:
            output = input * 3.28084
        elif conversion == 1:
            output = input * 0.3048
        self.output.set(output)
        return

root = Tk()
my_gui = MetersToFeetGUI(root)
root.mainloop()
