# Exit code 1 = invalid units
# Exit code 2 = invalid gender
# Exit code 3 = invalid lincence entered
# Exit code 4 = none number mass
# Exit code 5 = none number time
# Exit code 6 = none number drinks

# FUNCTION for calculating BAC
def calcBAC(A, r, W, t):
    # Error doing algorithm unless float cast first
    A = float(A)
    r = float(r)
    W = float(W)
    t = float(t)
    ans = A/(r*W)*100 - (0.00015*t)
    return ans


# Start of Main program
# Taking input from users for: gender, mass, status, time, drinks, units
# Try blocks to detect invalid input for number values
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

# Converting entered mass value to Grams
if(units == "Kg"):
    W = mass * 1000
elif(units == "lb"):
    W = mass * 453.592
else:
    print("Invalid units entered")
    exit(1)


# Determining conversion factor based on gender entered
if(gender == "m" or gender == "M"):
    r = 0.68
elif(gender == "f" or gender == "F"):
    r = 0.55
else:
    print("Unrecognised gender entered")
    exit(2)

# Calulate A based on standard drinks entered
A = drinks * 10
# BAC calulated by calcBAC function from start of this file
BAC = calcBAC(A, r, W, time)

# Print out the BAC for the user to see and for debugging
print("Estimated BAC is {0:.2f}".format(BAC))

# Inform the user if they are on an L or P licence what will happen if they drive
if(status == "L" or status == "P"):
    if(BAC > 0):
        print("License cancelled, interlock device")
        exit(0)
    else:
        print("Safe to drive")
        exit(0)

# Inform the user if they are on an FL licence what will happen if they drive
if(status == "FL"):
    if(BAC > 0.07):
        print("License cancelled, interlock device")
        exit(0)
    elif(BAC >0.05 and BAC<0.07):
        print("Fine and 10 demerit points")
        exit(0)
    else:
        print("OK to drive")
        exit(0)

# If we have not exited by now the licence entered was not recognised
print("Invalid licence entered")
exit(3)