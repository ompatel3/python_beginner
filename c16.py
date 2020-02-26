# Learning python 5e page 275
# chapter 9 Tuples, Files, and Everything Else
T=() # An empty tuple
T = (0,) # A one-item tuple (not an expression)
T = (0, 'Ni', 1.2, 3) # A four-item tuple
T = 0, 'Ni', 1.2, 3 # Another four-item tuple (same as prior line)
print(T)
T = ('Bob', ('dev', 'mgr')) # Nested tuples
T = tuple('spam') # Tuple of items in an iterable
print(T[1])
print(len(T))
print(T)
# T1 + T2 T * 3 # Concatenate, repeat
for x in T: print(x)
'spam' in T
print([x ** 2 for x in (1,2,3,4)])
print(T.index("m"))
print(T.count('Ni'))


# Tuples in Action
print((1, 2) + (3, 4)) # Concatenation
print((1, 2) * 4)  # Repetition
T = (1, 2, 3, 4) # Indexing, slicing
print(T[1:3])
x = (40) # An integer!
y = (40,) # A tuple containing an integer

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T) # Make a list from a tuple's items
tmp.sort()  # Sort the list
print(tmp)
T = tuple(tmp)
# Here, the list and tuple built-in functions are used to convert the object to a list and
# then back to a tuple

T = (1, 2, 3, 4, 5)
# List comprehensions can also be used to convert tuples.
L = [x + 20 for x in T]
print(L)

T = (1, 2, 3, 2, 4, 2)
print(T.index(2))  # Offset of first appearance of 2
print(T.index(2, 2)) # Offset of appearance after offset 2
print(T.count(2))  # How many 2s are there?
#  T[1] = 'spam'  can't change tuple itself!
T = (1, [2, 3], 4)
T[1][0] = 'spam' # This works: can change mutables inside
print(T)


# turple/ dic
bob = ('Bob', 40.5, ['dev', 'mgr'])  # Tuple record
bob[0], bob[2] # Access by position
bob = dict(name='Bob', age=40.5, jobs=['dev', 'mgr']) # Dictionary record
bob['name'], bob['jobs'] # Access by key
tuple(bob.values()) # Values to tuple
list(bob.items()) # Items to tuple list



# collection module
from collections import namedtuple
Rec = namedtuple('Rec', ['name', 'age', 'jobs']) # Make a generated class
bob = Rec(name='Bob', age=40.5, jobs=['dev', 'mgr']) # A named-tuple record
print(bob)
print(bob[0], bob[2])
print(bob.name, bob.jobs)

P = bob._asdict()  # # Dictionary-like form
P['name'], P['jobs'] # Access by key too

bob = Rec('Bob', 40.5, ['dev', 'mgr'])
name, age, jobs = bob  # Tuple assignment
for x in bob: print(x)
bob = {'name': 'Bob', 'age': 40.5, 'jobs': ['dev', 'mgr']}
(job, name, age) = bob.values() # Bob-job, 40.5-name,['dev', 'mgr']-age
print(name)
for x in bob: print(bob[x]) # Step though keys, index values
for x in bob.values(): print(x) # Step through values view



#Files
myfile = open('myfile.txt', 'w')
myfile.write('hello text file\n') # Write a line of text: string
myfile.write('goodbye text file\n')
myfile.close() # Flush output buffers to disk
myfile = open('myfile.txt') # Open for text input: 'r' is default
# read by line
print(myfile.readline())  # print line 1
print(myfile.readline())  # print line 2
print(myfile.readline()) # Empty string: end-of-file
# read all txt
print(open('myfile.txt').read()) # Read all at once into string
for line in open('myfile.txt'):
    print(line, end='')
data = open('data.bin', 'rb').read()
print(data)
print(data[4:8]) # Act like strings




#Storing Python Objects in Files
X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]
F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X, Y, Z)) # Convert numbers to strings
F.write(str(L) + '$' + str(D) + '\n') # Convert and separate with $
F.close()
print(open('datafile.txt').read())
F = open('datafile.txt')
line = F.readline()
print(line)
print(line.rstrip())  # Remove end-of-line
line = F.readline()
print(line)
parts = line.split(',') # Split (parse) on commas
print(parts)
int(parts[1]) # Convert from string to int
numbers = [int(P) for P in parts] # Convert all in list at once
print(numbers)

line = F.readline()
parts = line.split('$')
print(parts[0]) # Convert to any object type
objects = [eval(P) for P in parts] # Do same for all in list
print(objects)

# pickle!!!
# is a more advanced tool that allows us to store almost any Python object in a file directly
D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
import pickle
pickle.dump(D, F)  ## Pickle any object to file
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)  # Load any object from file
print(E)
print(open('datafile.pkl', 'rb').read())  # read in bin

# Storing Python Objects in JSON Format
#Python dictionary with nested structures is very similar to JSON data
name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print(rec)

import json
print(json.dumps(rec))
S = json.dumps(rec) # save
O = json.loads(S) # load
print(O)
print(O == rec)
json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
print(open('testjson.txt').read())
P = json.load(open('testjson.txt'))
print(P)

# import csv
# rdr = csv.reader(open('csvdata.txt'))
# for row in rdr: print(row)


# struct
F = open('data.bin', 'wb')
import struct
data = struct.pack('>i4sh', 7, b'spam', 8) # Make packed binary data
print(data)
F.write(data) # Write byte string
F.close()
print(open('data.bin', 'r').read())
print(open('data.bin', 'rb').read())
values = struct.unpack('>i4sh', data) # unpack to read # Convert to Python objects
print(values)


# File Context Managers
# with open(r'C:\code\data.txt') as myfile:
# myfile = open(r'C:\code\data.txt')
# try:
# for line in myfile:
# ...use line here...
# finally:
# myfile.close()

# won't change original data
L = [1,2,3]
D = {'a':1, 'b':2}
A = L[:]  ## Instead of A = L (or list(L))
B = D.copy()  # Instead of B = D (ditto for sets)
A[1] = 'Ni'
B['c'] = 'spam'
print(L, D)
print(A, B)

# or
X = [1, 2, 3]
L = ['a', X[:], 'b']
D = {'x':X[:], 'y':2}


# list same, string different obj
L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]
print(L1 == L2, L1 is L2)

S1 = 'spam'
S2 = 'spam'
print(S1 == S2, S1 is S2)

S1 = 'a longer string'
S2 = 'a longer string'
print(S1 == S2, S1 is S2)

print(bool(1), bool('spam'), bool({}))
print(type([1]) == type([]),type([1]) == list, isinstance([1], list))  # is [1] is a list?
# is f a function?
import types
def f(): pass
print(type(f) == types.FunctionType)

L = [1, 2, 3]
M = ['X', L, 'Y']
print(M)
L[1] = 0
print(M)
# if use copy
L = [1, 2, 3]
M = ['X', L[:], 'Y']
L[1] = 0
print(M)


# Repetition Adds One Level Deep
L = [4, 5, 6]
X = L * 4
Y = [L] * 4
print(X)
print(Y)
L[1] = 0  # only impacts Y
print(X)
print(Y)

L = [4, 5, 6]
Y = [list(L)] * 4  # won't change
L[1] = 0
print(Y)
Y[0][1] = 99 # change all
print(Y)


L = [4, 5, 6]
Y = [list(L) for i in range(4)]
print(Y)
Y[0][1] = 99  # onl change the first one
print(Y)

# Cyclic Data Structures!!!
L = ['grail']
L.append(L)
print(L)

# imutable turple
T = (1, 2, 3)
# T[2] = 4 # Error!
T = T[:2] + (4,) # OK: (1, 2, 4)