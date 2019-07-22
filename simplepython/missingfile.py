#!/usr/bin/python

try:
	data = open('unstruct_data1.txt')

	for line in data :
		print(line)

	data.close()
except IOError as err:
	print(str(err)) 



