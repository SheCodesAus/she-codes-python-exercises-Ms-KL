from tkinter.tix import InputOnly


name = input("what is your name? ")
hobby = input("what is your favourite hobby? ")

print(f"This is {name}, who likes {hobby}")

age = input(f"Hi {name},how old are you?" )

years_until_100 = 100 - int(age)

print(f"wow, you'll be 100 in {years_until_100} years! ")
