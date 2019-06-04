
'''
##1. read([size])方法 
f = open('123test.txt')
lines = f.read()
print(lines)
print(type(lines))
f.close()

'''

'''
##1. read([size])方法 
f = open('123test.txt')
sd = f.read()
print(sd)
print(type(sd))
f.close()
'''


'''
##2. readline()方法
import numpy as np
f = open('123test.txt')
line = f.readline()
print(type(line))
while line:
    print(line),
    line = f.readline()


print(np.shape(line))
f.close()
'''


'''
##3. readlines()方法
import numpy as np
f = open('123test.txt')
lines = f.readlines()
print(type(lines))
for line in lines:
    print(line),
print(np.shape(lines))
f.close()
'''

##3. readlines()方法
import numpy as np
f = open('123test.txt')
a = f.readlines()
print(type(a))
for b in a:
    print(b),
print(np.shape(a))
f.close()
