# cd C:\Users\krist\Desktop\KL_Projects\SheCodesPlus\python\scp_python_class\dictionaries\
# python q2.py

# Q2
# The dictionary below contains several colour names and a counter (defaulted to 0). 
# Your task is to iterate over a list of colours and 
# keep track of the number of times each colour has occurred by 
# updating the corresponding counter in this dictionary.

colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
}


# colours = [
#     "purple",
#     "red",
#     "yellow",
#     "blue",
#     "purple",
#     "orange",
#     "blue",
#     "purple",
#     "orange",
#     "green"
# ]



colours = [
    "orange",
    "purple",
    "blue",
    "yellow",
    "green",
    "green",
    "purple",
    "purple",
    "green",
    "blue",
    "green",
    "orange",
    "purple",
    "blue",
    "green",
    "orange",
    "orange",
    "red",
    "yellow",
    "yellow"
]


def colour_counting (colour_counts, colours):
    '''
    Args:
        A dictionary and a list
    '''
    result = ""
    for colour in colours:
        for colour_counter in colour_counts.keys():
            if colour == colour_counter:
                colour_counts[colour] +=1

    for colour_counter, count in colour_counts.items():
        result += f"{colour_counter}: {count}\n"

    return result


print(colour_counting(colour_counts, colours))