###
#
#

import re

def is_valid_extension(filename):   # Check if file extension has four characters
    return bool(re.search(r'\.[a-zA-Z0-9]{4}$', filename)) # Match extensions of 4 characters



# Main program
if __name__ == "__main__":
    try:
        with open('files.txt', 'r') as file:  # Open file
            for line in file:     # Read each line in the file
                filename = line.strip() # Strip whitespace
                if is_valid_extension(filename):  # Check if name has is valid - 4 characters
                    print(filename)
    except FileNotFoundError:
        print("The file 'files.txt' was not found.")
