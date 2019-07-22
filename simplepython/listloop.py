# Simple example to loop in the list of items

futureskills = ["3D Printing", "Artifical Intelligence", "BlockChain", "IOT"]

# list through each of the items using for loop using identifier

for skills in futureskills:
    print(skills)


count = 0

while count < len(futureskills):
    print(futureskills[count])
    count = count + 1
