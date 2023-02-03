# for_loops_exercises.py

# ------ Q1 --------
# Ask the user for a number. Use a for loop to print the times tables for that number.

# number = int(input("Enter a number: "))
# count = 1

# for i in range(0,number):
#     print(number * count)
#     count+=1


# ------ Q2 --------
# DO THIS

# Ask the user for a number. 
# Use a for loop to sum from 0 to that number.

number = int(input("Enter a number: "))
total = 0
numb = 0

for numb in range(0,number): 
    total += numb
    numb +=1

print (total)

# ------ Q3 --------
# Q3) Given a list, use a for loop to sum all the numbers in the list.