###
#
#

import csv

file_name = 'clothing.csv'


try:            # Open file
    with open(file_name, mode='r', newline='', encoding='utf-8') as file:

        reader = csv.DictReader(file)    # Read csv file; map rows to dictionary
        

        print("Products with Price < 60 and Stock < 40")       # Print header
        print("=======================================")
        

        for row in reader:
            price = float(row['Price']) # Extract  values and check conditions
            stock_quantity = int(row['Stock_Quantity'])
            

            if price < 60 and stock_quantity < 40: # Check if price is less than 60 and stock is less than 40
                # Print product details
                print(f"Product ID: {row['Product_ID']}, Name: {row['Product_Name']}, Price: {row['Price']}, Stock: {row['Stock_Quantity']}")
                
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
