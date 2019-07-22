#!/usr/bin/python

dad = []
kid = []

try:
	data = open('unstruct_data.txt')
	for line in data:
		try:
			(person, line_spoken) = line.split(':')
			if person == 'Dad ':
				dad.append(line_spoken)
			elif person == 'Kid ':
				kid.append(line_spoken)
		except ValueError as VE:
			print(VE)
			pass
	data.close()
except IOError as IO:
	print(IO)
print(dad)
print(kid)
