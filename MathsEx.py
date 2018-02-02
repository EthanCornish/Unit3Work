
# Formula
# h = (q+((3(m+1))/5)+k+(k/4)+(j/4)-2j)%7

# h = day of the week, 0 = Saturday, 1 = Sunday... 14 = February
# q = date
# m = month (3 = month)
# j = zero based century   (Year//100)           (2018) = 20
# k = the year of the century (year%100)        (2018) = 18
# If in January or Feb k-1, (minus one year)
# Ask for the year, month and date

# Asks the user for the date
q = int(input('What is the day of the month? (In numerical form please, e.g. 31'))
# Asks the user for the month in a numerical form
m = int(input('What month is it? (In numerical form please, e.g. 12'))
# Asks the user for the year
y = int(input('What year is it?'))
# Uses the year to find j and k
j = (y // 100)
k = (y % 100)
#Creates a new variable to replace m in the formula that can be manipulated
n = m
# Checks if the month is jan or feb
if m < 3:
    n = m + 12           # Adds 12 to m
    k = k - 1            # Subtracts one from k

# Formula
h = int((q+((13*(n+1))//5)+k+(k//4)+(j//4)-(2*j))%7)
print(h)

# Takes output from formula to print a day of the week.
if h == 0:
    print('The {0}/{1}/{2} is a Saturday.'.format(q, m, y))
elif h == 1:
    print('The {0}/{1}/{2} is a Sunday.'.format(q, m, y))
elif h == 2:
    print('The {0}/{1}/{2} is a Monday.'.format(q, m, y))
elif h == 3:
    print('The {0}/{1}/{2} is a Tuesday.'.format(q, m, y))
elif h == 4:
    print('The {0}/{1}/{2} is a Wednesday.'.format(q, m, y))
elif h == 5:
    print('The {0}/{1}/{2} is a Thursday.'.format(q, m, y))
elif h == 6:
    print('The {0}/{1}/{2} is a Friday.'.format(q, m, y))
else:
    print('You did not enter valid information.')
