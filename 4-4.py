###
#
#

with open('it_company.csv', 'r') as file:   # Open file and read
    lines = file.readlines()  # Read lines from file into list

index = 0   # Variable for position in list


# Loop to print 5 lines 
while index < len(lines):   # 
    for i in range(index, min(index + 5, len(lines))): # Print next lines
        print(lines[i], end='')  # The `end=''` prevents `print()` from adding an extra newline


    input("\nPress Enter key...")       # Wait for Enter


    index += 5  # Next lines
