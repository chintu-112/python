#!/usr/bin/python


with open('ram.txt') as data:
	a = data.readline().strip().split(',')
	print(a)

with open('test_data.txt') as testdata:
	b = testdata.readline().strip().split(':')
	print(b)

with open('test_data.txt') as testdata:
	for line in testdata:
		c = line.strip().split(':')
		print(c)




