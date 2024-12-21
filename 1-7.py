###
# Reads the entire contents of a file
#

def read_from_file(name):   # Reads the entire contents of a file
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('car_park.txt')   # Reads the entire file and splits lines into array
file_lines = file_content.splitlines()


total = 0       # Calculates the total number of cars parked
for line in file_lines:
   total += int(line)  # convert each line to an integer and add to total

print('Total cars parked:', total)
