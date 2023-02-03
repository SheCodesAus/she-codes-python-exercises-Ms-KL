# Q5) 
# Modify your code from the previous exercise to save both the English name and RGB code in a list as the
# value for the corresponding hex code.

# dict = {key:value}
# dict.keys()
# dict.values()
# dict.items()


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
            colours[line[1]] = [line[0],line[2]]
            for hex, values in colours.items():
                print(f"{hex}: {values}")

    return

colour_dictionary("colours_20_simple.csv")