
print('This program will calculate your approximate BAC level.\nNote: This is an approximate and not 100% accurate.')

gender = input('What is your gender, M = Male or W = Woman.')
mass = float(input('What is your mass in kilograms or pounds?'))
unit = input('What unit did you enter your mass in, Metric or Imperial?')
time = float(input('How many hours has it been since you started drinking?'))
drinks = float(input('How many standard drinks have you consumed?'))
status = input('What is your driving status, L = Learner, P = Probationary, FL = Full Licence')

if unit == 'Metric':
    W = mass * 1000
else:
    W = mass * 453.592

if gender == 'M':
    r = 0.68
else:
    r = 0.55

A = drinks * 10
BAC = (A/(r*W))*100-(0.00015*time)

print(BAC)

if status == 'L' or status == 'P':
    if BAC > 0:
        print('Your BAC is greater than 0.\nLicense Cancelled, Interlock Device Installed.')
    else:
        print('You are ok to drive.')

if status == 'FL':
    if BAC > 0.7:
        print('Your BAC is greater than 0.7.\nLicense Cancelled, Interlock Device Installed.')
    elif 0.05 < BAC < 0.07:
        print('Your BAC is between 0.05 and 0.07.\nFine and 10 Demerit Points.')
    else:
        print('You are ok to drive.')
