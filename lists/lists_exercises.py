# lists_exercises.py

# Q1) Given the list of foods below, output:
# 1. The first item in the list.
# 2. The third item in the list.
# 3. The last item in the list.
# 4. The first three items in the list.
# 5. The last three items in the list.
# 6. The last item in the sublist.

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

# print(foods[0])
# print(foods[2])
# print(foods[-1])
# print(foods[0:3])
# print(foods[-3:])
# print(foods[-4][-1])

# Q2) Format and print the following list:
mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"],
]



line = 0
print (f"{mailing_list[line][0]}: {mailing_list[line][1]}")


while line < ((len(mailing_list)-1)):
    line += 1

    print (f"{mailing_list[line][0]}: {mailing_list[line][1]}")
