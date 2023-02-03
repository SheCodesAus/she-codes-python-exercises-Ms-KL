# conditionals are true or false
# ctrl K

# is_raining = True
# is_cold = False
# print(is_raining)
# print (is_raining and not is_cold) -TRUE
# print (not is_raining and not is_cold) - FALSE

# temperature = 16
# print (temperature < 18)
# wind_chill = 3
# print (wind_chill > 4)
# print (temperature - wind_chill < 16)

# name = "Kristy"
# print(name == "Kristy")
# #compares name to string in print using ==
# print (name!= "Kristy")
# # != is not

is_raining= True
wind_chill = 5




if is_raining:
    print ("Take an umbrella")
elif wind_chill > 4:
    print ("Bring a Jacket")
# elif and if statement above both must be true for this to work
else:
    print("Do not take an umbrella")




# if is_raining:
#     print ("Take an umbrella")
# if is_raining and wind_chill > 4:
#     print ("bring a jacket")
# else:
#     print("Do not take an umbrella")




# if is_raining:
#     print ("Take an umbrella")
#     if is_raining and wind_chill > 4:
#         print ("bring a jacket")
# #same as below
# if is_raining and wind_chill > 4:
#     print("is the same")