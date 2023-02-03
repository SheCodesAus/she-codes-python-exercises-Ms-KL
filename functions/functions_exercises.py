# Windows Powershell
# cd c://currentfolderpath
# python currentfile.py

# ------------------- Q1
# Write a function that takes a temperature in fahrenheit and returns the temperature in celsius.

# def convert_f_to_c(temp_in_f):
#     '''
#     Write a function that converts f to c
#     (32°F − 32) × 5/9 = 0°C
#     '''
#     temp_in_c = (temp_in_f - 32) * .5556
#     return temp_in_c 

# print(convert_f_to_c(32))
# print(convert_f_to_c(0))
# print(convert_f_to_c(350))


# ------------------- Q2
# Write a function that accepts one parameter (an integer) and returns True when that parameter is odd and False when that parameter is even.

# def odd_or_even(integer):
#     '''
#     Write a function that accepts one parameter (an integer) and returns True when that parameter is odd and False when that parameter is even.
#     '''
#     if integer % 2 == 0:
#         result = False
#         # even
#     else:
#         result = True
#         # odd

#     return result

# print(odd_or_even(2))
# print(odd_or_even(7))
# print(odd_or_even(-1))

# ------------------- Q3
# Write a function that returns the mean of a list of numbers.

def mean_list (list_a):
    sum = 0
    for i in list_a:
        sum = sum+i
    mean = sum / len(list_a)

    return mean

print(mean_list([4,3,2,6]))
print(mean_list([10,5,6]))
