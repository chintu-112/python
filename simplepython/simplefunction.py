# This is a simple example of function to read a list of lists

academics = [2000, "Secondary School", ["Subject", ["Math", "Physic", "Chem"]]]

# Function for repeatitive task


def iterate(academics):
    for item in academics:
        if isinstance(item, list):
            iterate(item)
        else:
            print(item)
            

iterate(academics)

