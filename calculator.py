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
                split_list[i] = float(split_list[i])

        if input_numbers == "q": #Allowing user to quit out of program
            break
        #Conditions for different operations
        else: 
            if split_list[0] == "+":
                split_list = split_list[1:]
                added_numbers = add(split_list)
                print added_numbers
            elif split_list[0] == "-":
                split_list = split_list[1:]
                subt_numbers = subtract(split_list)
                print subt_numbers
            elif split_list[0] == "*":
                split_list = split_list[1:]
                mult_numbers = multiply(split_list)
                print mult_numbers
            elif split_list[0] == "/":
                split_list = split_list[1:]
                div_numbers = divide(split_list)
                print div_numbers
            elif split_list[0] == "power":
                split_list = split_list[1:]
                power_numbers = power(split_list)
                print power_numbers
            elif split_list[0] == "mod":
                mod_numbers = mod(split_list[1], split_list[2])
                print mod_numbers
            elif split_list[0] == "square":
                split_list = split_list[1:]
                square_numbers = square(split_list)
                print square_numbers
            elif split_list[0] == "cube":
                split_list = split_list[1:]
                cube_numbers = cube(split_list)
                print cube_numbers

calculator()