# Classes Examples


# Creating a class to be referred to as dog
class Dog:

    # Class variable shared by all instances
    kind = 'canine'

    # __init__ means that everything in it only occurs for that instance of Dog
    # self refers to the name of the instance
    # Name argument is the argement given when the class and function was called
    # Tricks is created and seperate for each instance of Dog
    def __init__(self, name):
        self.name = name
        self.tricks = []

    # Allows the user to add infomation to the list
    # Trick arguement is given when the class function is called
    def add_trick(self, trick):
        self.tricks.append(trick)


# Defining instances of dog
# The argument is name
# The __init__ function runs because it is a separate instance of Dog being called
d = Dog('Fido')
e = Dog('Buddy')

# Value before the dot is the instance of Dog class, Between . and ( is the function being called, and the arguement
#       given is the argument in the function that is not self
d.add_trick('back flip')
e.add_trick('sit')
e.add_trick('stand')

# Printing the instance of dog does not work
print(d.name)
print(d.kind)
print(d.tricks)

print(e.name)
print(e.kind)
print(e.tricks)
print('\n')


class Cat:
    def __init__(self, name):
        self.name = name
        self.vaccines = []

    def addVaccine(self, vaccine):
        self.vaccines.append(vaccine)

f = Cat('Mittens')
g = Cat('Snowy')

f.addVaccine('FCV')
f.addVaccine('FVR')
g.addVaccine('None')

print(f.name)
print(f.vaccines)

print(g.name)
print(g.vaccines)