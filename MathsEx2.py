import math

print('This program will find the hypotanuse on a right angle triangle.')
print('You will be asked for the length of side a and b please give the sides in the same unit without the unit.')

a = int(input('What is the length of side a?'))
b = int(input('What is the length of side b?'))

c = math.sqrt((a**2)+(b**2))
print('The hypotenuse is {0:.2f}'.format(c))