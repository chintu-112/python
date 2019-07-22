# This is a simple example of list containing another list

academics = [2000, "Secondary School", ["Subject", ["Math", "Physic", "Chem"]]]

# Printing the academics List

for item in academics:
    print(item)


# Check if an object is a list and print it

for item in academics:
    if isinstance(item, list):
        for each_item in item:
            print(each_item)
    else:
        print(item)