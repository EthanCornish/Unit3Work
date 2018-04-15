from tkinter import Tk, Label, Button, LEFT, RIGHT, W

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is our first GUI!")

        self.greet_button = Button(master, text="Greet", command=self.greet)

        self.close_button = Button(master, text="Close", command=master.quit)

        # Default Pack
        # self.label.pack()
        # self.greet_button.pack()
        # self.close_button.pack()

        # Side Pack
        # self.label.pack()
        # self.greet_button.pack(side=LEFT)
        # self.close_button.pack(side=RIGHT)

        # Grid arrange
        self.label.grid(columnspan=1, sticky=W)
        self.greet_button.grid(row=1)
        self.close_button.grid(row=1, column=1)

    def greet(self):
        print("Greetings!")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
