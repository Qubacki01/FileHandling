###
# Checks the correctness of username and password
#

import re

# Read username and password from the keyboard
username = input("Enter username: ")
password = input("Enter password: ")

# Patterns (criteria) for username and password
username_pattern = r'^[a-z]{6,}$'  # Username must be at least 6 characters long, only lowercase letters
password_pattern = r'^[A-Za-z0-9_]{8,}$'  # Password must be at least 8 characters long, letters, digits, and underscores

# Check if username and password are ok
username_match = re.match(username_pattern, username)   # If match pattern
password_match = re.match(password_pattern, password)

# Print results
if username_match and password_match:
    print("Username and password are valid.")
else:
    print("Invalid username or password.")
