# Windows Powershell
# cd c://currentfolderpath
# python currentfile.py

# ----------------------- Q1
# Ask the user for a number. 
# Use a for loop to print the times tables for that number.

# number = int(input("Enter a number: "))
# count = 1

# for i in range(0,number):
#     product = number * count
#     print(f"{number} * {count} = {product}")
#     count+=1

# ----------------------- Q2
# Ask the user for a number. 
# # Use a for loop to sum from 0 to that number.

# enter_number = int(input("Enter a number: "))

# running_total = 0
# count=1

# for number in range(0,enter_number):
#     running_total = running_total + count
#     count+=1

# print(running_total)

        # running_total + count = running total
        # 0 + 1 = 1
        # 1 + 2 = 3
        # 3 + 3 = 6
        # 6 + 4 = 10
        # 10 + 5 = 15
        # 15 + 6 = 21

# ----------------------- Q3
# Given a list, use a for loop to sum all the numbers in the list.

# random_numbers = [3, 5, 9, 1]
# sum = 0

# for i in range(0,len(random_numbers)):
#     sum = sum + random_numbers[i]

# print(sum)

    # sum + number_in_list = sum
    # 0 + 3 = 3
    # 3 + 5 = 8
    # 8 + 9 = 17
    # 17 + 1 = 18

# ----------------------- Q4
# Use a for loop to format and print the following list:

# mailing_list = [
# ["Chilli", "chilli@thechihuahua.com"],
# ["Roary", "roary@moth.catchers"],
# ["Remus", "remus@kapers.dog"],
# ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
# ["Ivy", "noreply@goldendreamers.xyz"],
# ]

# for i in range(0,len(mailing_list)):
#     print(f"{mailing_list[i][0]}: {mailing_list[i][1]}")

    # Chilli: chilli@thechihuahua.com
    # Roary: roary@moth.catchers
    # Remus: remus@kapers.dog
    # Prince Thomas of Whitepaw: hrh.thomas@royalty.wp
    # Ivy: noreply@goldendreamers.xyz