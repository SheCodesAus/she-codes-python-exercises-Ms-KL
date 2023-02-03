#  ----------------------  Q1  ---------------------- 
# Q1 Kate’s cat, Roary, loves catching moths. Write a program that determines whether or not it is time for Roary to catch moths.

# moths_in_house = False

# if moths_in_house == True:
#     print ("Get the moths!")
# else:
#     print ("No threats detected")

# ----------------------- Q2  ---------------------- 
# Q2 But Roary can’t actually get the moths by herself! Amend the previous program to determine whether or not it is time for Roary to go moth hunting

# moths_in_house = False
# mitch_is_home = True

# if moths_in_house == True:
#     if mitch_is_home == True:
#         print ("Hoooman! Help me get the moths!")
#     else:
#         print ("Meooooooooooooow! Hissssss!")

# else:
#     if mitch_is_home == True:
#         print ("Climb on Mitch!")
#     else:
#         print ("No Threats Detected")

# ALT

# moths_in_house = False
# mitch_is_home = False

# if moths_in_house and mitch_is_home:
#     print ("Hoooman! Help me get the moths!")

# if moths_in_house and not mitch_is_home:
#     print("Meooooooooooooow! Hissssss!")

# if mitch_is_home and not moths_in_house:
#         print ("Climb on Mitch")

# else:
#     if not moths_in_house and not mitch_is_home:
#         print ("no threats detected")

# ALT

# moths_in_house = False
# mitch_is_home = True

# if moths_in_house and mitch_is_home:
#     print ("Hoooman! Help me get the moths!")

# elif moths_in_house and not mitch_is_home:
#     print("Meooooooooooooow! Hissssss!")

# elif mitch_is_home and not moths_in_house:
#         print ("Climb on Mitch")

# else:
#     if not moths_in_house and not mitch_is_home:
#         print ("no threats detected")

# ----------------------- Q3  ---------------------- 
# Q3 Write a program that implements the algorithm for Red Light Cameras.

# light_colour = "red"
# # green, amber
# car_detected = False

# if car_detected and light_colour == "red":
#     print ("Flash!")

# else:
#     print ("do nothing")

# ----------------------- Q4  ---------------------- 
# Q4 Write a program that asks the user for their height, and determines whether or not they are tall enough to ride the rollercoaster, which has a height requirement of 120cms.

# height = 160

# if height >= 120:
#     print ("Hop on!")
# else:
#     print ("Sorry not today :(")

#  ---------------------- Q5  ---------------------- 
# Write a program that asks the user to enter their username and password, and outputs a success message if they are correct, or a failure message if they are incorrect.

# username = "fleur"
# password = "password123"

# enter_username = input("Username: ")
# enter_password = input("Password: ")

# if username == enter_username and password == enter_password:
#     print("Correct!")
# else:
#     print ("Incorrect!")

# ---------------------- Q6  ---------------------- 
# Write a program that asks the user to enter their email address and checks whether it is valid or not. For the purpose of this exercise, you can make the assumption that a valid email address contains a “@” symbol and a “.” symbol.


enter_email = input ("Email: ")

if "@" and "." in enter_email:
    print ("Valid email address")

else:
    print ("Invalid email address")

