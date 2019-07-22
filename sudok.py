#!/usr/local/bin/python

import random

sudok = {}

print(sudok)

sudok = {'topL' : ' ', 'topM' : ' ', 'topR' : ' ', \
	'midL' : ' ', 'midM' : ' ', 'midR' : ' ', \
	'botL' : ' ', 'botM' : ' ', 'botR' : ' ' \
}

print(sudok)

def printBoard(sudok1):
	print(sudok1['topL'] + "||" + sudok1['topM'] + "||" + sudok1['topR'])
	print("=" + "||" + "=" + "||"+ "=")
	print(sudok1['midL'] + "||" + sudok1['midM'] + "||" + sudok1['midR'])
	print("=" + "||" + "=" + "||" + "=")
	print(sudok1['botL'] + "||" + sudok1['botM'] + "||" + sudok1['botR'])

printBoard(sudok)

## Retrieve two random number

random1 = str(random.randint(1,9))
random2 = str(random.randint(1,9))

print(random1)
print(random2)

while random1 == random2:
	print("Try another random ")
	random2 = str(random.randint(1,9))
	if random1 != random2:
		break

items = list(sudok.keys())
print(items)

randItem1 = items[random.randrange(len(items))]
randItem2 = items[random.randrange(len(items))]

while randItem1 == randItem2:
	print("Try another random item")
	randItem2 = items[random.randrange(len(items))]
	if randItem1 != randItem2:
		break

print(randItem1)
print(randItem2)

sudok[randItem1] = random1
sudok[randItem2] = random2

print(sudok)
#printBoard(sudok)


print("Start Playing the Game : ")
print(len(sudok)-2)
for i in range(len(sudok)-2):
	printBoard(sudok)
	loc = input("Enter the location : ")

	if sudok[loc] == " ":
		val = input("Enter the value : ")

		while val == random1 or val == random2 or val not in range(1,9):
			print("Enter a different value : ")
			val = input("Enter the value : ")
			if val != random1 and val != random2 and val in range(1,9):
				break
			else:
				continue

		sudok[loc] = val
	else:
		print("Please select empty location : ")
		break
		
