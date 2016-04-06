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
        if input_numbers == "q": #Allowing user to quit out of program
            break
        else:
            int_one = int(split_list[1]) #Reassigning index1 as an integer
            int_two = int(split_list[2]) #Reassigning index2 as an integer
            if split_list[0] == "+":
                added_numbers = add(int_one,int_two)
                print added_numbers
            elif split_list[0] == "-":
                subt_numbers = subtract(int_one,int_two)
                print subt_numbers
            elif split_list[0] == "*":
                mult_numbers = multiply(int_one,int_two)
                print mult_numbers
            elif split_list[0] == "/":
                div_numbers = divide(int_one,int_two)
                print div_numbers
            # elif split_list[0] == "square":
            # elif split_list[0] == "cube":
            # elif split_list[0] == "power":
            # elif split_list[0] == "mod":

        

calculator()