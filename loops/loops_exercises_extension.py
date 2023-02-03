# Windows Powershell
# cd c://currentfolderpath
# python currentfile.py


# ------------------- Q1 --------------
# Q1) Below is a list of foods and their prices per unit:

# from tabulate import tabulate

# groceries = [
# ["Baby Spinach", 2.78],
# ["Hot Chocolate", 3.70],
# ["Crackers", 2.10],
# ["Bacon", 9.00],
# ["Carrots", 0.56],
# ["Oranges", 3.08]
# ]


# Ask the user how many units of each item they bought, then output the corresponding receipt.
# For the input below, assume that the input is provided in the same order as defined in the list above.

# data = []
# cost = 0
# how_many = 0

# for item in groceries:
#     how_many = int(input(f"How many {item[0]} did you buy? "))
#     cost=how_many*item[1]
#     data.append([item[0],f"${cost:,.2f}"])
#     print(data)

# print("==== Izzy's Food Emporium ====")
# print((tabulate(data)))
# print("============================")

# --- ALT   -------- (no tabulate)

# groceries = [
# ["Baby Spinach", 2.78],
# ["Hot Chocolate", 3.70],
# ["Crackers", 2.10],
# ["Bacon", 9.00],
# ["Carrots", 0.56],
# ["Oranges", 3.08]
# ]


# cost = 0
# how_many = 0
# total = 0
# data = []


# for item in groceries:
#     how_many = int(input(f"How many {item[0]} did you buy? "))
#     cost=how_many*item[1]
#     total = total+cost
#     data.append([item[0],f"${cost:,.2f}"])

# print("                            ")
# print("======Izzy's Food Emporium======")

# for line in data:
#     print(f"{line[0]:<20}\t{line[1]}")
# print("================================")
# print(f"\t\t\t${total:,.2f}")


# ------------------- Q2 --------------
# Q2) Ask the user to enter a string. 
# Output the string one character at a time, as well as it’s position in the string

# enter_word = input("Please enter a string: ")

# for i in range(len(enter_word)):
#     print(i, enter_word[i])
#     # prints index (due to range) and the word index based on iteration


# ------------------- Q3 --------------
# Q3) Ask the user for a number and use this to generate a pyramid of that height.

enter_height = int(input("Pyramid size: "))

for i in range(0,enter_height):
    i+=1
    print("*"*i)

# ------------------- Q4 --------------
# Q4) Ask the user for a number and use this to generate a (different) pyramid of that height.

number_stars = -1
enter_height = int(input("Pyramid size for triangle: "))
distance = 0

for i in range(0,enter_height):
    distance = enter_height - i - 1 
    number_stars = number_stars + 2
    print (" "*distance + "*"*number_stars)


