# Part 2 Types and operations p1----p108
# list
L = [123, 'spam', 1.23]  # A list of three different-type objects
print(len(L))  # Number of items in the list
print(L[0])  # Indexing by position
print(L + [4, 5, 6]) # Concat/repeat make new lists too
print(L * 2)  # Concat/repeat make new lists too
L.append('NI')  # Growing: add object at end of list
print(L)  # L changed
L.pop(0) # Shrinking: delete the first item in L
print(L)
M = ['bb', 'aa', 'cc']
M.sort()  # sort aphabetically
print(M)
M.reverse()  # reverse the sequence
print(M)

#Nesting
M = [[1, 2, 3], [4, 5, 6],[7, 8, 9]] # A 3 × 3 matrix, as nested lists Code can span lines if bracketed
print(M)
print(M[1])  # Get row 2
print(M[1][2])  # Get row 2, then get item 3 within the row


# a list comprehension expression
col2 = [row[1] for row in M]  # the second item in each row
print(col2)
print([row[1] + 1 for row in M])  # every second item in each row plus 1
print([row[1] for row in M if row[1] % 2 == 0])  # the second item in each row which mod 2=0
diag = [M[i][i] for i in [0, 1, 2]]  # return diag
print(diag)
doubles = [c * 2 for c in 'spam'] # ssppaamm
print(doubles)
print(list(range(4)))  # 0-3
print(list(range(-6, 9, 2)))  # −6 to +8 by 2
print([[x ** 2, x ** 3] for x in range(4)])
print([[x, x / 2, x * 2] for x in range(-6, 7, 2) if x > 0])
G = [sum(row) for row in M]  # Create a list of row sums
print(G)
G = (sum(row) for row in M)  # Create a generator of row sums
print(next(G))
print(next(G))
print(next(G))
# map function
print(list(map(sum, M)))  #  Map sum over items in M
# comprehension syntax can also be used to create sets and dictionaries:
print({sum(row) for row in M}) # Create a set of row sums
print({i : sum(M[i]) for i in range(3)})  # Creates key/value table of row sums
# order
print([ord(x) for x in 'spaam'])  # List of character ordinals
print({ord(x) for x in 'spaam'})  # Sets remove duplicates
print({x: ord(x) for x in 'spaam'}) # Dictionary keys are unique
print((ord(x) for x in 'spaam'))  # Generator of values)

# dictionaries
D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
print(D['food'])
D['quantity'] += 1
print(D)
D = {}
D['name'] = 'Bob' # Create keys by assignment
D['job'] = 'dev'
D['age'] = 40
print(D)
bob1 = dict(name='Bob', job='dev', age=40)  # Keywords
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40])) # Zipping

# Nesting dictionaries Revisited
rec = {'name': {'first': 'Bob', 'last': 'Smith'}, 'jobs': ['dev', 'mgr'], 'age': 40.5}
print(rec['name'])  # 'name' is a nested dictionary
print(rec['name']['last'])  # Index the nested dictionary
rec['jobs']  # 'jobs' is a nested list
rec['jobs'][-1]   # Index the nested list
rec['jobs'].append('janitor')  # Expand Bob's job description in place
print(rec)

# if test
D = {'a': 1, 'b': 2, 'c': 3}
if not 'f' in D:  # Python's sole selection statement
    print('missing')
if not 'f' in D:
    print('missing')
    print('no, really...')  # Statement blocks are indented
value = D.get('a', 0)  # Index but with a default to check a is in the D: o True 1 False
print(value)
value = D['x'] if 'x' in D else 0 # if/else expression form


# for loops
D = {'a': 1, 'b': 2, 'c': 3}
Ks = list(D.keys())  # Unordered keys list
print(Ks)
Ks.sort()  # Sorted keys list
print(sorted(D))
print(Ks)
for key in Ks: # Iterate though sorted keys
    print(key, '=>', D[key])  # <== press Enter twice here (3.X print)
for key in sorted(D):
    print(key, '=>', D[key])
for c in 'spam':
    print(c.upper())  # printing the uppercase version of each as it goes

# while loop
x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

# Iteration and Optimization
squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
squares = []
for x in [1, 2, 3, 4, 5]: # This is what a list comprehension does
    squares.append(x ** 2)  # Both run the iteration protocol internally
print(squares)

# Tuples
T = (1, 2, 3, 4) # A 4-item tuple
print(len(T))
print(T + (5, 6)) # Concatenation
T[0]  # Indexing, slicing, and more
T.index(4) # Tuple methods: 4 appears at offset 3
T.count(4) # 4 appears once
# Tuples are immutable  T[0] = 2 wrong!
T = (2,) + T[1:] # Make a new tuple for a new value
print(T)
T = 'spam', 3.0, [11, 22, 33]
print(T[1])
print(T[2][1])
# AttributeError: 'tuple' object has no attribute 'append'T.append(4)

# Files
import os
print(os.getcwd())
f = open('data.txt', 'w')  # Make a new file in output mode ('w' is write)
f.write('Hello\n')  # Write strings of characters to it
f.write('world\n')
f.close()

f = open('data.txt') # 'r' (read) is the default processing mode
text = f.read()  # Read entire file into a string
print(text)
print(text.split())  # File content is always a string
for line in open('data.txt'): print(line)
dir(f)  # check method in f
help(f.seek)  # more details about a specific method

# Binary Bytes Files
import struct  #  Python’s struct module can both create and unpack packed binary data
packed = struct.pack('>i4sh', 7, b'spam', 8) # Create packed binary data
print(packed)
help(struct.pack)
file = open('data.bin', 'wb') # Open binary output file
file.write(packed) # Write packed binary data
file.close()
data = open('data.bin', 'rb').read()
print(data)  # 10 bytes, unaltered
print(data[4:8]) # Slice bytes in the middle
print(list(data)) # A sequence of 8-bit bytes
struct.unpack('>i4sh', data) # Unpack into objects again


#Unicode Text Files
S = 'sp\xc4m'  # Non-ASCII Unicode text
print(S[2])  # Sequence of characters
file = open('unidata.txt', 'w', encoding='utf-8')  # Write/encode UTF-8 text
file.write(S) # 4 characters written
file.close()
text = open('unidata.txt', encoding='utf-8').read() # Read/decode UTF-8 text
print(text)
raw = open('unidata.txt', 'rb').read()  # Read raw encoded bytes
print(raw)
print(text.encode('utf-8'))  # Manual encode to bytes
print(raw.decode('utf-8')) # Manual decode to str
print(text.encode('latin-1'))  # Bytes differ in others
print(text.encode('utf-16'))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16'))


# Other Core Types
X = set('spam')  # Make a set out of a sequence
print(X)
Y = {'h', 'a', 'm'} # Make a set with set literals
print(X, Y)  # A tuple of two sets without parentheses
print(X & Y)  # Intersection
print(X | Y)  # Union
print(X - Y)  # Difference
print(X > Y)  # Superset
print({n ** 2 for n in [1, 2, 3, 4]})  # Set comprehensions
print(list(set([1, 2, 1, 3, 1]))) # Filtering out duplicates (possibly reordered)
print(set('spam') - set('ham'))  # Finding differences in collections
set('spam') == set('asmp')  # Order-neutral equality tests (== is False)
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])  # in

# decimal numbers
1 / 3 # Floating-point
(2/3) + (1/2)
import decimal # Decimals: fixed precision
d = decimal.Decimal('3.141')
print(d)
decimal.getcontext().prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

# fraction
from fractions import Fraction  # Fractions: numerator+denominator
f = Fraction(2, 3)
print(f)
print(f+1)
print(f + Fraction(1, 2))

# Booleans
print(1 > 2, 1 < 2)  # < , >
bool('spam')  # Object's Boolean value
X = None # None placeholder
print(X)
L = [None] * 100 # Initialize a list of 100 Nones
print(L)


#Break Your Code’s Flexibility
print(type(L))  # types are classes, and vice versa
print(type(type(L)))
if type(L) == type([]): # Type testing, using [] list
    print('yes')
if type(L) == list: # Using the type name
    print('yes')
if isinstance(L, list): # Object-oriented tests
    print('yes')

# object-oriented programming in Python
class Worker:
    def __init__(self, name, pay):  # Initialize when created
        self.name = name   # self is the new object
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]  # Split string on blanks

    def Raise(self, percent):
         self.pay *= (1.0 + percent)  # Update pay in place
         return self.pay
bob = Worker('Bob Smith', 50000)
print(bob.name)
print(bob.pay)
print(bob.lastName())
print(bob.Raise(0.4))