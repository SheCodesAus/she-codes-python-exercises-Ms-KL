# cd C:\Users\krist\Desktop\kl_projects\shecodesplus\python\scp_python_class\w2_b

# python functions_playground.py


# def create_greeting(name):
#     greeting = f"Hello, {name}"
#     return greeting

# print(create_greeting("Chilli"))
# print(create_greeting("Daisy Sparkles"))

# ------ Ex

# def product_calculation(number):
#     '''
#     Write a function that takes an integer as a parameter and returns that integer multiplied by 3
#     '''
#     result = number * 3
#     return f"{number} * {3} = {result}"

# print(product_calculation(3))
# print(product_calculation(10))


# ------ Ex

# def convert_cm_to_in(length_cm):
#     '''
#     Write a function that converts cm to inches 
#     '''
#     length_in_inches = length_cm / 2.54
#     return length_in_inches

# print(convert_cm_to_in(20))

# ------ Ex

# def convert_in_to_cm(length_in):
#     '''
#     Write a function that converts inches to cms 
#     '''
#     length_in_cm = length_in * 2.54
#     return length_in_cm

# print(convert_in_to_cm(6))

# ------ Ex

def calculate_mean(a,b):
    # multiple variables
    total = a + b
    mean = total / 2
    return mean

print(calculate_mean(3,4))

# don't use global for variables. 
# Instead call existing function and reassign to a different variable

# eg: 
# use_mean = calculate_mean(3,4)
# instead of global mean

# ------ Ex

def calculate_mean(a,b):
    # multiple variables
    total = a + b
    multiply = a * b
    mean = total / 2
    return mean, total, multiply

print(calculate_mean(3,4))







