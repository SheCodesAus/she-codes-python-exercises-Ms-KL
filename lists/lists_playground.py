# # lists_playground.py

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard list"]
# print(len(chilli_wishlist))
# # prints number of items in list

# print(chilli_wishlist[4])
# # finds the index / location of item in the list
# # [error. Indexing starts at 0. Last item is actually #3
# # [0] first item on list
# # [-1] last item on list
# # [-2] second last item on list

# print(chilli_wishlist)

# print(chilli_wishlist[0:2])
# # prints list from location 0 to 2. But 2 is not included.
# # prints igloo and chicken

# print(chilli_wishlist[1:3])
# # prints chicken and donut toy
# # starts with location 1, then 2, ignores 3.

# chilli_wishlist[1] = "carrot"
# # replaces item at index
# # chicken replaced by carrot

# chilli_wishlist.index("igloo")
# # finds igloo in the list and returns the index #

# chilli_wishlist.append("dig mat")
# # adds dig mat to the end of the list
# # append only adds one

# chilli_wishlist.extend(["kong", "tennis ball", "crocodile toy"])
# # adds more than 1 item to list at end

# chilli_wishlist.insert(1,"peanut butter")
# # inserts "peanut butter" @ index [1] and moved all other items down

# chilli_wishlist.pop()
# # no specification will remove last item from list
# # specify something to remove that item

# chilli_wishlist.pop(2)
# # deletes item at index number
# # don't specify index

# chilli_wishlist.remove("kong")
# # specify the value (not index) to remove

# chilli_wishlist.insert(-2,"donkey")
# # slots in before the specified index and pushes the other 2 down
# # ends up in position -3

# del chilli_wishlist[0:3]
# # removes items from 0 - 2 (ignores 3)

# print(chilli_wishlist)


# ----------

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard list"]
# print(chilli_wishlist)

# if "tennis ball" in chilli_wishlist:
#     print("chilli would like a tennis ball")
# else:
#     print("chilli doesn't feel like playing fetch")

# if len(chilli_wishlist) > 3:
#     # returns the len it and compares it to 8
#     print("you want alot of stuff!")


# ----------

# CHALLENGE:

# chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard list"]
# print(chilli_wishlist)

# if "blueberries" in chilli_wishlist:
#     print("Chilli has blueberries")
# else: 
#     chilli_wishlist.append("blueberries")
# print(chilli_wishlist)

# alt:
# if "blueberries" not in chilli_wishlist:
#     chilli_wishlist.append("blueberries")
# else: 
#     print("Chilli has blueberries")
# print(chilli_wishlist)

# ----------

chilli_wishlist = [
    ["igloo"], 
    ["donut toy", "tennis ball", "crocodile toy"],
    ["chicken", "peanut butter"],
    ["cardboard box", "kong", "dig mat"]
]

print (chilli_wishlist[2])
print (chilli_wishlist[2][1])
# finds item @ index 2, and item 1 within it
# peanut butter

# change 2nd item in 3rd list
chilli_wishlist[2][1] = "collar"
print(chilli_wishlist)

# add another sublist at the end of list
chilli_wishlist.append(["blueberries", "watermelon"])
print(chilli_wishlist)

# alt
chilli_wishlist.extend([["blueberries", "watermelon"]])
print(chilli_wishlist)
