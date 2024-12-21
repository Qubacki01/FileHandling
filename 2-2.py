###
# Writes Seven Wonders of the World to a file
#

seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

file_name = 'seven_wonders.txt' # Name of the file to write to

seven_wonders.sort()    # Sort data alphabetically

with open(file_name, 'w') as file:  # Write data to the file
    for item in seven_wonders:
        file.write(item + '\n')     # \n > new line
