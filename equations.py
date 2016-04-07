def add(num_list):
    summ = num_list[0]
    num_list = num_list[1:]
    for num in num_list: 
        summ += num
    return summ

def subtract(num_list):
    subt = num_list[0]
    num_list = num_list[1:]
    for num in num_list:
        subt -= num
    return subt

def multiply(num_list):
    product = 1
    for num in num_list:
        product *= num 
    return product

def divide(num_list):
    quotient = num_list[0]
    num_list = num_list[1:]
    for num in num_list:
        quotient /= num
    return quotient

def square(num_list):
    double_list = []
    for num in num_list:
        double = num*num
        double_list.append(double)
    return double_list

def cube(num_list):
    cube_list = []
    for num in num_list:
        cube = num*num*num
        cube_list.append(cube)
    return cube_list

def power(num_list):
    power_list = []
    base = num_list[::2]
    exponent = num_list[1::2]
    #Loop through index of base list and match to index of exponent list
    for i in range(len(base)):
        power_num = base[i]**exponent[i]
        power_list.append(power_num)
    return power_list 

def mod(num_list):
    mod_list = []
    mod1 = num_list[::2]
    mod2 = num_list[1::2]
    #Loop through index of mod1 list and match to index of mod2 list
    for i in range(len(mod1)):
        remainder = mod1[i]%mod2[i]
        mod_list.append(remainder)
    return mod_list