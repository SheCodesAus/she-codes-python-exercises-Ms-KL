# Q4) 
# Read the colour data from colours_20_simple.csv 
# and save the data in a dictionary 
#   where the key is the hex code and 
#   value is the corresponding English name.

# dict = {key:value}
# dict.keys()
# dict.values()
# dict.items()

# step 1: open and read csv
# step 2: save items in dictionary (instead of list)
# step 3:               dict = {hex:name) = {BEBD7F: Green beige, C2B078: Beige, etc
# 
# 
# 
#BEBD7F: Green beige
#C2B078: Beige
#C6A664: Sand yellow
#E5BE01: Signal yellow
#CDA434: Golden yellow
#A98307: Honey yellow

import csv

def colour_dictionary (csv_file):
    """
    docstring insert
    """
    colours = {}
    with open (csv_file, encoding="utf-8") as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile)
        for line in reader:
            colours[line[1]] = line[2]
            for hex, english in colours.items():
                print(f"{hex}: {english}")

    return

colour_dictionary("colours_20_simple.csv")