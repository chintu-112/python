#!/usr/bin/python

data = open('test_data.txt')

for line in data :
	(person, line_spoken) = line.split(':')
	print(person)
	print(line_spoken)

data.close()
