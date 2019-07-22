#!/usr/bin/python

dad = []
kid = []

with open('unstruct_data.txt') as data:
    for line in data:
        try:
            (person, line_spoken) = line.split(':')
            line_spoken = line_spoken.strip()
            if person == 'Dad ':
                dad.append(line_spoken)
            elif person == 'Kid ':
                kid.append(line_spoken)
            else:
                pass
        except ValueError as VE:
            print(str(VE))

print(dad)
print(kid)

### Save the data and kid list to a file
try:
    #dadfile = open('dadfile.txt', 'w')
    #kidfile = open('kidfile.txt', 'w')
    with open('withdadfile.txt', 'w') as withdadfile:
        print(dad, file=withdadfile)
    with open('withkidfile.txt', 'w') as withkidfile:
        print(kid, file=withkidfile)

    #dadfile.close()
    #kidfile.close()
except IOError as IOE:
    print('File Error' + str(IOE))
