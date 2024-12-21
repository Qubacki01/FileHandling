###
#
#

with open("integer_power.txt", "w") as file:   # Open file in write
    for i in range(1, 101): 
        second_power = i ** 2    # Calculate second and third powers
        third_power = i ** 3
        
        result = f"{i},{second_power},{third_power}"   # Change to string
        print(result)
        

        file.write(result + "\n")  # Save the result to the file
