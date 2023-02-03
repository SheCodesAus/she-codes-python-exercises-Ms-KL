# Windows Powershell
# cd c://currentfolderpath
# python currentfile.py

#-----------Q1
# Write a program that reads in colours_20_simple.csv 
# and output the colour data.

# import csv

# with open("colours_20_simple.csv ", encoding="utf-8") as csv_file:
#     # utf-8 translates unicode characters and turn into binary so computer can understand
#     reader = csv.reader (csv_file)
#     for line in reader:
#         print(line[0],line[1],line[2])

#-----------Q2
# Write a program that reads in colours_20_simple.csv and outputs the colour data in order English, Hex then RGB.

# import csv

# with open("colours_20_simple.csv ", encoding="utf-8") as csv_file:
#     # utf-8 translates unicode characters and turn into binary so computer can understand
#     next(csv_file)
#     reader = csv.reader (csv_file)
#     for line in reader:
#         print(f"{line[2]}, Hex: {line[1]}, RGB: {line[0]}")


#-----------Q3
# Write a program that reads in colours_20.csv and output the colour data in order English, Hex then RGB.

# import csv

# with open("colours_20.csv ", encoding="utf-8") as csv_file:
# #utf-8 translates unicode characters and turn into binary so computer can understand
#     next(csv_file)
#     reader = csv.reader (csv_file)
#     for line in reader:
#         print(f"{line[4]}, Hex: {line[2]}, RGB: {line[1]}")

#-----------Q4
# Using the same colour csv files, write a program that outputs the number of times each of the following
# colours appear in the English Name:
# ● red
# ● green
# ● blue
# ● yellow

# import csv
# red = 0
# green = 0
# blue = 0
# yellow = 0

# with open("colours_213.csv ", encoding="utf-8") as csv_file:
# #utf-8 translates unicode characters and turn into binary so computer can understand
#     next(csv_file)
#     reader = csv.reader (csv_file)
#     for line in reader:
#         if "red" in line[4]:
#             red+=1
#         elif "green"in line[4]:
#             green+=1
#         elif "blue"in line[4]:
#             blue+=1
#         elif "yellow"in line[4]:
#             yellow+=1

# print(f"Red: {red}")
# print(f"Green: {green}")
# print(f"Blue: {blue}")
# print(f"Yellow: {yellow}")

#-----------Q5
# galaxies.py contains data about 82 different galaxies and their velocities (km/sec). 
# Using this data, output the galaxy with the slowest velocity, and the galaxy with the highest velocity.

# import csv

# galaxy_1 = 0
# galaxy_2 = 0
# min_velocity = 0
# max_velocity = 0
# galaxies = []
# galaxies_int = []

# with open("galaxies.csv ", encoding="utf-8") as csv_file:
# #utf-8 translates unicode characters and turn into binary so computer can understand
#     next(csv_file)
#     reader = csv.reader (csv_file)
#     for line in reader:
#         galaxies.append((line))
#         for elm in galaxies:
#             galaxies.sort(key = lambda galaxies: galaxies[1])
#             # this sorts the 2nd element in list, but as a string. cannot sort as integer.

# print(galaxies)
# print(f"Galaxy {galaxy_1} has the min velocity of {min_velocity}km/sec.\nGalaxy {galaxy_2} has the max velocity of {max_velocity}km/sec. ")

# ---- alt

import csv

galaxy_min = 0
galaxy_max = 0
galaxies = []

with open("galaxies.csv ", encoding="utf-8") as csv_file:
#utf-8 translates unicode characters and turn into binary so computer can understand
    next(csv_file)
    reader = csv.reader (csv_file)
    for line in reader:
        line_int = [int(line[0]),int(line[1])]
        galaxies.append((line_int))
    galaxy_min = (min(galaxies))
    galaxy_max = (max(galaxies))

print(f"Galaxy {galaxy_min[0]} has the min velocity of {galaxy_min[1]}km/sec.\nGalaxy {galaxy_max[0]} has the max velocity of {galaxy_max[1]}km/sec. ")

# use this if the value range is different
# eg: galaxy 1 doesn't necessarily have lowest velocity
    # print(max(galaxies, key=lambda x: x[1]))
    # print(min(galaxies, key=lambda x: x[1]))