

# for_loops_playground.py

# ------- EX 1 ------- 

# for num in range(10):
#     print(num)
# # prints 0 - 9

# for num in range(1,11):
#     print(num)
# # prints range starting @ 1 and ends at 11 (10)

# for num in range (0,11,2):
#     print(num)
# # 0 = start position
# # 11 = end position
# # 2 = step

# for num in range (0,101):
#     print(num)
# # can print 1 - 100

# # ALT: 
# # can do for num in range (101)

# ------- EX 2 ------- 

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

# # for item in range (len(chilli_wishlist)):
# #     print(chilli_wishlist[item])

# # for each item in the range upto the length of the wishlist, print each item within the list. 
# # AKA: @ each iteration print a wishlist item (loop)

# # ALT:
# # for item in chilli_wishlist:
# #     print (item)

# for item in chilli_wishlist:
#     print (f"Chilli wants {item}")

# ------- EX 3 ------- 

# chilli_wishlist = [
# ["igloo"],
# ["donut toy", "tennis ball", "crocodile toy"],
# ["chicken", "peanut butter"],
# ["cardboard box", "kong", "dig mat"]
# ]

# for category in chilli_wishlist:
#     print(f"this is a category: {category}")
#     for item in category:
#         print (f"this is an item: {item}")

# ------- EX 4 ------- 

# guess = ""
# while guess != "a":
#     guess = input("Guess again: ")

# counter = 10

# while counter <=10:
#     print(counter)
#     counter +=1

# ctrl + c = interrupt

# ------- EX 5 ------- 

# enter_name = input("Enter a name: ")
# # ALT: enter_name = "name" <--- DRY

# while enter_name != "":
#     enter_name = input("Enter a name: ")


