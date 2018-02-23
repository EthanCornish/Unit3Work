
# Get the filename from the user
print('Enter the name of the file to be read')
fname = input(':')      # fname is the name of the file to be read
list = []   # Create a new list

# Open the file specified by the user
try:
    #   variable containing file = open(name of file, 'mode (read, write, append)
    f = open(fname, 'r')        # 'r' means read only,  'w' means write (overwrights previous data)
                                # 'a' means append to end of file
except FileNotFoundError:
    print('File does not exist')
    exit(0)

# Read line by line
for line in f:          # For each line in the file
    # Strip the new lines
    line = line.strip('\n')     #S trip pulls the thing in brackets off
    # Printing the line
    print(line)  # Can only read through once. Once read file must be closed and reopened.
    list.append(line)   # Each line is an element in the list

print(list)
# Closing
f.close()


# Open file for write
f = open(fname, 'a')    # Same file as earlier

# Add a new line to the file so input is on a different line
f.write('\n')

# Write to the file
f.write(input('Add a new line to the bottom of the file'))      # Adds directly to the end of the file

# Close the file
f.close()