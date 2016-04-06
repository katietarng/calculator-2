"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import * #from the arithmetic file import everything


# Your code goes here

def calculator():
    """Calculating input with different operations"""
    while True: 
        input_numbers = raw_input() #Prompting user to add input here
        split_list = input_numbers.split(" ") #splits input into list
        for i in range(len(split_list)):
            if i > 0:
                split_list[i] = int(split_list[i])
        if input_numbers == "q": #Allowing user to quit out of program
            break
        else: 
            if split_list[0] == "+":
                added_numbers = add(split_list[1], split_list[2])
                print added_numbers
            """elif split_list[0] == "-":
                subt_numbers = subtract()
                print subt_numbers
            elif split_list[0] == "*":
                mult_numbers = multiply()
                print mult_numbers
            elif split_list[0] == "/":
                div_numbers = divide()
                print div_numbers
            elif split_list[0] == "power":
                power_numbers = power()
            elif split_list[0] == "mod":
       
            elif split_list[0] == "square":
                square_numbers = square()
                print square_numbers
            # elif split_list[0] == "cube":
        """

calculator()