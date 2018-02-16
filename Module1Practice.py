# exit(1) = invalid input


# Function for calculating BAC
def calcBAC(A, r, W, time):
    # To stop an algorithmic error
    A = float(A)
    r = float(r)
    W = float(W)
    t = float(time)
    ans = (A/(r*W))*100 -(0.00015*t)
    return ans

print('This program will calculate your approximate BAC level.\nNote: This is an approximate and not 100% accurate.')

# Receive input for the user

correct = 'no'      # Create a variable to check if the input is correct
# Receive input for the gender, repeatedly ask until getting desirable input
while correct == 'no':
    gender = input('What is your gender, M = Male or F = Female.')
    if gender == 'M' or gender == 'F':
        correct = 'yes'
correct = 'no'

# Receive input for the mass and if getting a ValueError ask again
try:
    mass = float(input('What is your mass in kilograms or pounds?'))
except ValueError:
    print('You did not enter a correct value. Please enter either a whole number or a decimal with no characters.')
    mass = float(input('What is your mass in kilograms or pounds?'))

# Receive input for the unit, repeatedly ask until getting desirable input
while correct == 'no':
    unit = input('What unit did you enter your mass in, Metric or Imperial?')
    if unit == 'Metric' or unit == 'Imperial':
        correct = 'yes'
correct = 'no'

# Receive input for the time and if getting a ValueError ask again
try:
    time = float(input('How many hours has it been since you started drinking?'))
except ValueError:
    print('You did not enter a correct value. Please enter either a whole number or a decimal with no characters.')
    time = float(input('How many hours has it been since you started drinking?'))

# Receive input for the amount of drinks and if getting a ValueError ask again
try:
    drinks = float(input('How many standard drinks have you consumed?'))
except ValueError:
    print('You did not enter a correct value. Please enter either a whole number or a decimal with no characters.')
    drinks = float(input('How many standard drinks have you consumed?'))

# Receive input for the status, repeatedly ask until getting desirable input
while correct == 'no':
    status = input('What is your driving status, L = Learner, P = Probationary, FL = Full Licence')
    if status == 'L' or status == 'P' or status == 'FL':
        correct = 'yes'


# Convert the given mass to W for formula applying specified manipulations
if unit == 'Metric':
    W = mass * 1000
elif unit == 'Imperial':
    W = mass * 453.592
else:
    print('You did not give correct input')
    exit(1)

if gender == 'M':
    r = 0.68
elif gender == 'F':
    r = 0.55
else:
    print('You did not give correct input')
    exit(1)

# Set variable A as specified
A = drinks * 10

# Calculate BAC according to given formula
BAC = calcBAC(A, r, W, time)
print('BAC = {0:.2f}'.format(BAC))

print('\n\n')       # Print 2 New Lines for output neatness

# Check if the driving status given is L or P
if status == 'L' or status == 'P':
    # Check if the BAC is greater than 0, if it is give output saying they can't drive otherwise say they can
    if BAC > 0:
        print('Your BAC is greater than 0\nLicense Cancelled, Interlock Device Installed.')
    else:
        print('You are ok to drive.')

# Check if the driving status given is FL
if status == 'FL':
    # Check if BAC is greater than 0.7, between 0.5 and 0.7 or less than 0.5 and give correct output according to -
    # Module instructions
    if BAC > 0.07:
        print('Your BAC is greater than 0.7.\nLicense Cancelled, Interlock Device Installed.')
    elif 0.05 < BAC < 0.07:
        print('Your BAC is between 0.05 and 0.07.\nFine and 10 Demerit Points.')
    else:
        print('You are ok to drive.')
