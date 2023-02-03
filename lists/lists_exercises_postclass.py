# lists_exercises_postclass.py

# ---------------------- Q1 Given the list of foods below, output: ---------------------- 

# foods = [
# "orange",
# "apple",
# "banana",
# "strawberry",
# "grape",
# "blueberry",
# ["carrot", "cauliflower", "pumpkin"],
# "passionfruit",
# "mango",
# "kiwifruit"
# ]

# # 1. The first item in the list:

# print(foods[0])

# # 2. The third item in the list.

# print(foods[2])

# # 3. The last item in the list.

# print(foods[-1])

# # 4. The first three items in the list.

# print(foods[0:3])

# # 5. The last three items in the list.

# print(foods[-3:])

# # 6. The last item in the sublist.

# print(foods[-4][-1])


# ---------------------- Q2 Format and print the following list: ---------------------- 

from ast import Name


mailing_list = [
["Chilli", "chilli@thechihuahua.com"],
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Ivy", "noreply@goldendreamers.xyz"],
]

# line = 0

# print (f"{mailing_list[line][0]}: {mailing_list[line][1]}")

# line += 1

# print (f"{mailing_list[line][0]}: {mailing_list[line][1]}")

# line += 1

# print (f"{mailing_list[line][0]}: {mailing_list[line][1]}")

# line += 1

# print (f"{mailing_list[line][0]}: {mailing_list[line][1]}")

# line += 1

# print (f"{mailing_list[line][0]}: {mailing_list[line][1]}")

# ALT For Loop ------

# line = 0

# for lines in mailing_list:
#     if line <= len(mailing_list):
#         print(f"{mailing_list[line][0]}: {mailing_list[line][1]}")
#         line += 1

# ALT While Loop ------

# line = 0

# while line < ((len(mailing_list)-1)):
#     print (f"{mailing_list[line][0]}: {mailing_list[line][1]}")
#     line += 1

# ---------------------

# Q3 Ask the user for three names, add them to a list, then print the list.

# name_list = []
# name1 = input("Enter a name: ")
# name_list.append(name1)
# name2 = input("Enter a name: ")
# name_list.append(name2)
# name3 = input("Enter a name: ")
# name_list.append(name3)
# print(name_list)

# ALT while loop ------

# name_list = []
# number_names = 3

# while len(name_list) <= (number_names-1):
#     name = input("Enter a name: ")
#     name_list.append(name)

# print(name_list)

# ---------------------

# Q4 Using the following starter code:

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
# d = []
# e = []

# Produce the following lists:

# d.extend((a,b,c))
# print (d)
# e.extend((d[0][0],d[0][1],d[0][2],d[1][0],d[1][1],d[1][2],d[2][0],d[2][1],d[2][2]))
# print(e)

# ALT for loop and range ----------

# d.extend((a,b,c))
# print (d)

# for i in range (1,10):
#     e.append(i)

# print(e)

# ALT: POP ---------------

# d.extend((a,b,c))
# print (d)
# e.extend(d.pop([0][0]))
# e.extend(d.pop([0][0]))
# e.extend(d.pop([0][0]))
# print(e)

# ALT: Nirali inspo ----------

    #  + adds items to list without brackets

# d.extend((a,b,c))
# print (d)
# e.extend(a + b + c)
# print(e)

# ALT: Nirali - BEST ----------

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
# d = [a,b,c]
# e = []
# e = a + b + c
# print (d)
# print (e)

# ALT: Nirali part 2 ----------

# list3 = []
# list3.extend(a)
# list3.extend(b)
# list3.extend(c)
# print(list3)

# ALT: Sue Lim ----------

# code_list_a = [1, 2, 3]
# code_list_b = [4, 5, 6]
# code_list_c = [7, 8, 9]
# code_list_d = []
# code_list_e = []
# print(f"{code_list_a} {code_list_b} {code_list_c}")
# code_list_a.append(code_list_b.pop(-3))
# code_list_a.append(code_list_b.pop(-2))
# code_list_a.append(code_list_b.pop(-1))
# code_list_a.append(code_list_c.pop(-3))
# code_list_a.append(code_list_c.pop(-2))
# code_list_a.append(code_list_c.pop(-1))
# print(code_list_a)
