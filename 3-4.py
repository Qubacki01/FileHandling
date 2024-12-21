###
# Calculates the total value of money spent
#

import re  # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email w/ UTF-8
with open(email_file, 'r', encoding='utf-8') as file:
    email = file.read()

# regular expression pattern for amounts with €
pattern = r'€(\d+)'  # Match €; Match 1 or more digits

# extract numbers from email
amounts = re.findall(pattern, email)    # Create list

# calculate the total purchases
total = 0
for amount in amounts:
    total += int(amount)  # Convert to float

# print the result
print(f"Total money spent: €{total}")
