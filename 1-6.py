###
# Reads the entire contents of a file
#

def read_from_file(name):       # Read file
   with open(name, 'r') as file:
      content = file.read()
   return content

file_content = read_from_file('countries.txt')  # Reads the entire file

file_lines = file_content.splitlines()  # Splits the entire file contents into lines and stores them in an array

sorted_lines = sorted(file_lines)   # sorts the array alphabetically


for line in sorted_lines:
   print(line)
