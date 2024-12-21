###
# Creates a shopping list based on product names
# entered from the keyboard.
#

# Shopping list file name
shopping_list = 'shopping_list.txt'


# Adds product name at the end of a shopping list
def add_product(file_name, product_name):
    with open(file_name, 'a') as file:     # Open file in append mode
        file.write(product_name + '\n')    # Writes the product name with a new line


# Takes next product name from the keyboard
product = ""
while product != "0":
    product = input('Enter product name (0 stops): ')
    if product == '0':
        break        # Stops entering product names when '0' is entered
    else:
        add_product(shopping_list, product)
