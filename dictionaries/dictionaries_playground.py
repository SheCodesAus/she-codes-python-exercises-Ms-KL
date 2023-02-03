groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08,
}

print(groceries)
# print all groceries

print(groceries["Baby Spinach"])
# access key Baby Spinach to get value of $
print(groceries["Baby Spinach"])

groceries["Avacadoes"] = 1.00
# adds avo to dict
print(groceries)

groceries ["Hot Chocolate"] = 2.70
#change the value of the key hot chocolate

del groceries["Crackers"]
# deletes the item from dict

print (groceries)




# --- these 2 give the same result:

# 1
for item in groceries:
    print (f"{item}: ${groceries[item]}")
    # use groceries[item] to get value

# 2
for item, price in groceries.items():
    # item = placeholder
    # items = function to help index against the dictionary
    print(f"{item}: ${price}")


    # why dictionary:
    # good for avoiding duplicates
    # good for categorising information (author, title, etc)

## lookup enumerate (list)

