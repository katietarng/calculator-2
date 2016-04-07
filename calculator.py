"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from equations import * #from the equations file import everything


def calculator():
    """Calculating input with different operations"""
    while True: 
        input_numbers = raw_input() #Prompting user to add input here
        split_list = input_numbers.split(" ") #splits input into list

        #Loop through list to change indices 1+ to integer
        for i in range(len(split_list)): 
            if i > 0:
                split_list[i] = int(split_list[i])

        if input_numbers == "q": #Allowing user to quit out of program
            break
        #Conditions for different operations
        else: 
            if split_list[0] == "+":
                added_numbers = add(split_list[1], split_list[2])
                print added_numbers
            elif split_list[0] == "-":
                subt_numbers = subtract(split_list[1], split_list[2])
                print subt_numbers
            elif split_list[0] == "*":
                mult_numbers = multiply(split_list[1], split_list[2])
                print mult_numbers
            elif split_list[0] == "/":
                div_numbers = divide(split_list[1], split_list[2])
                print div_numbers
            elif split_list[0] == "power":
                power_numbers = power(split_list[1], split_list[2])
                print power_numbers
            elif split_list[0] == "mod":
                mod_numbers = mod(split_list[1], split_list[2])
                print mod_numbers
            elif split_list[0] == "square":
                square_numbers = square(split_list[1])
                print square_numbers
            elif split_list[0] == "cube":
                cube_numbers = cube(split_list[1])
                print cube_numbers

calculator()