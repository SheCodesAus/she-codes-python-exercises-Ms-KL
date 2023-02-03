# cd C:\Users\krist\Desktop\kl_projects\shecodesplus\python\scp_python_class\w2_b

# python csv_files_playground.py

import csv

# with open ("2016_pilbara.csv") as csv_file:
# # reference file and rename to csv_file
#     reader = csv.reader(csv_file)
#     # can read the csv file. Reads each line as a list.
#     # every row / line is a list. Reads each line
#     for line in reader:
#         print(line)
    
#     # above reads the data. We want to put this into a list so we can access / reference as required.

population = []

with open("2016_pilbara.csv", encoding="utf-8") as csv_file:
    # utf-8 translates unicode characters and turn into binary so computer can understand
    reader = csv.reader (csv_file)
    for line in reader:
        population.append(line)
        # append each line from reader into list population

# print (population)

# --------------- EX 1

for age_group in population:
    # for each item in list (age_group), print the 0 and 1 index.
    print(f"{age_group[0]} {age_group[1]}")

# --------------- Ex 2

with open("population.csv", mode="w", encoding="utf-8") as csv_file:
    # open csv file, writable mode, encode, save as easy name.
    csv_writer = csv.writer(csv_file, delimiter=",")
    # creates csv file population, sets delimiter as ,

    for age_group in population:
        csv_writer.writerow ([age_group[1],age_group[0]])
        # writerow = function in csv library