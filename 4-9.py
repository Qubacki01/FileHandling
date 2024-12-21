###
#
#

import csv

file_name = 'it_company.csv'


try:            # Open file
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:

        reader = csv.DictReader(file)   # Read csv file; map rows to dictionary
                                        

        print("GRAPHIC DESIGNERS")      # Print header
        print("=================")
        

        for row in reader:
            if row['Job Title'] == 'Graphic Designer':  # Check if job title is 'Graphic Designer'
                print(f"{row['First Name']} {row['Last Name']},{row['Email']}")   # Print first name, last name, email
                
except FileNotFoundError:
    print(f"'{file_name}' was not found.")
