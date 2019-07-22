#!/usr/bin/python

dad = []
kid = []

try:
    data = open('unstruct_data.txt')

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
    data.close()
except IOError as IOE:
    print('The data file is missing' + str(IOE))

print(dad)
print(kid)

### Save the data and kid list to a file
try:
    dadfile = open('dadfile.txt', 'w')
    kidfile = open('kidfile.txt', 'w')

    print(dad, file=dadfile)
    print(kid, file=kidfile)

    #dadfile.close()
    #kidfile.close()
except IOError as IOE:
    print('File Error' + str(IOE))
finally:
    dadfile.close()
    kidfile.close()
