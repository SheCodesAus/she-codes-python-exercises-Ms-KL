# cd C:\Users\krist\Desktop\KL_Projects\SheCodesPlus\python\scp_python_class\dictionaries\
# python q1.py

# Q1) 
# The dictionary below represents the cost of individual items in a supermarket. 
# A separate dictionary is given in the table below, 
# this dictionary represents the quantity of each item purchased. 
# Use these two dictionaries to write a program that 
# outputs the cost of each item.

prices = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
}

# quantity = {
#     "Baby Spinach": 1,
#     "Hot Chocolate": 3,
#     "Crackers": 2,
#     "Bacon": 1,
#     "Carrots": 4,
#     "Oranges": 2
# }

quantity = {
    "Baby Spinach": 2,
    "Hot Chocolate": 1,
    "Crackers": 4,
    "Bacon": 0,
    "Carrots": 8,
    "Oranges": 5
}

# dicts
# https://www.w3schools.com/python/python_dictionaries_loop.asp

# https://stackoverflow.com/questions/15619096/add-zeros-to-a-float-after-the-decimal-point-in-python

def groceries_rcpt (prices, quantity):
    '''
    args:
    2x dictionaries
    '''
    rcpt = ""
    for item, price in prices.items():
        number = quantity[item]
        # [item] finds the current item from prices dict in the current loop and finds the same key in the quantity dict and returns the value associated.
        cost = format((number * price),'.2f')
        rcpt += f"{number} {item} @ ${price} = ${cost}\n"
    
    return rcpt

print(groceries_rcpt(prices, quantity))