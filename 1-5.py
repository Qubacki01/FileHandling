###
#
#

with open('countries.txt', 'r') as file:        
    for index, line in enumerate(file, start=1):    # Go over the lines; index start from 1
        print(f"{index}. {line.strip()}")
