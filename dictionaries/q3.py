# cd C:\Users\krist\Desktop\KL_Projects\SheCodesPlus\python\scp_python_class\dictionaries\
# python q3.py

# Q3)
# Given the list of names below, create a dictionary where each key is a name and the value is the number of times that name occurs in the list.


names = [
    "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
    "Joy", "Katie", "Maddie", "Tash", "Nic",
    "Rachael", "Bec", "Bec", "Tabitha", "Teagen",
    "Viv", "Anna", "Catherine", "Catherine", "Debby",
    "Gab", "Megan", "Michelle", "Nic", "Roxy",
    "Samara", "Sasha", "Sophie", "Teagen", "Viv"
]

def name_counting(names):
    '''
    Args:
    a list of names
    '''
    result = ""
    name_counter = {}


    # for name in names:
    #     if name not in name_counter:
    #         name_counter[name] = 1
    #     else:
    #         name_counter[name] +=1

    # for name_count, count in name_counter.items():
    #     result += f"{name_count} {count}\n"

    # ---- ALT comprehension -----
    counter = name_counter[name]
    
    counter = 1 for name in names if name not in name_counter else counter +=1

    result += f"{name_count} {count}\n" for name_count, count in name_counter.items()


    
    return result

print(name_counting(names))

# names = [
#     "Miranda", "Sophie", "Emily", "Taylor", "Anne",
#     "Djuarli", "Anika", "Rosie", "Miranda", "Taylor",
#     "Abby", "Sarah", "Teagen", "Abby", "Abby",
#     "Maddie", "Miranda", "Rosie"
# ]
