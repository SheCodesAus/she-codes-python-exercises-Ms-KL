# Windows Powershell
# cd c://currentfolderpath
# python currentfile.py


# ------------- Q1
# Continuously ask the user to enter a number until they provide a blank input. 
# Output the sum of all the numbers

# sum = 0
# enter_number = 0

# while enter_number != "":
#     enter_number = input("Enter a number: ")
#     if enter_number != "":
#         sum = int(enter_number) + sum
# print(sum)

# ------------- Q2
# Ask the user to enter a number. 
# Print all the odd numbers between 0 and that number (inclusive).

# enter_number = int(input("Enter a number: "))
# count = 1

# while count <= enter_number:
#     print (count)
#     count+=2

# ------------- Q3
# Select a number. 
# Ask the user to enter a number, output whether their number is less than or greater than the selected number. 
# Repeat this process until the user guesses the correct number.

guess_number = int(input("Guess the number: "))
winning_number = 55

while guess_number is not winning_number:
    if guess_number > winning_number:
        print("Too high!")
    else:
        print("Too low!")
    guess_number = int(input("Guess again: "))

else:
    print("correct!")