#!/usr/bin/env python3
#from testClass import*

#test = Hello()

#test.speak()

import sys

print("In test: ", sys.argv[1:])
# print(sys.path)

# print(double(5))

file = open("output.txt", 'w')
file.write(str(sys.argv[1:]))
file.close()
#print(file.readline())
