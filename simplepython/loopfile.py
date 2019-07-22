#!/usr/bin/python

data = open('test_data.txt')

for line in data :
	print(line, end='')

# Rewind to the first line and read the data again

data.seek(0)

for line in data :
        print(line, end='')

data.close()

