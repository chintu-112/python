#/usr/bin/python

data = open('test_data.txt')

print(data.readline(), end='')
print(data.readline(), end='')

print(data.readline())
print(data.readline())

data.close()


