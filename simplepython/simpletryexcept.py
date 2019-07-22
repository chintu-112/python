#!/usr/bin/python

data = open('unstruct_data.txt')


for line in data:
	try:
		(person, line_spoken) = line.split(':')
		print(line)
	except:
		pass

data.close()

