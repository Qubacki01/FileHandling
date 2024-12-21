###
# Prints employees employed in a specified position.
#

file_name = 'it_company.csv'

job_title = 'Software Engineer'

with open(file_name, 'r') as file:
    header = file.readline()    # Read first line and skip it

    employee_number = 1

   
    for line in file:   # Read line from file
        fields = line.strip().split(',') # Split line by commas (CSV format)

        if job_title in fields[2]:  # Check if job_title = Software Engineer
            print(f"{employee_number}. {line.strip()}")
            employee_number += 1
