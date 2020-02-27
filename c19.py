# Learning python 5e page 392 - 415
# CHAPTER 13 while and for Loops

# while test: statements
#     if test: break # Exit loop now, skip to else if present
#     if test: continue # Go to top of loop now, to test1
# else:
#     statements # Run if we didn't hit a 'break'

# for loop
# for target in object: # Assign object items to target
# #     statements # Repeated loop body: use target
# # else: # Optional else part
# #     statements # If we didn't hit a 'break'

#
# for target in object: # Assign object items to target
#     statements
#     if test: break # Exit loop now, skip else
#     if test: continue # Go to top of loop now
# else:
#     statements # If we didn't hit a 'break'


for x in ["spam", "eggs", "ham"]:
    print(x, end=' ')
prod = 1
for item in [1, 2, 3, 4]: prod *= item
print(prod)
S = "lumberjack"
for x in S: print(x, end=' ') # Iterate over a string
T = ("and", "I'm", "okay")
for x in T: print(x, end=' ') # Iterate over a tuple

# tuple assignment
T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:print(a, b)

# dic assignment
D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])  # Use dict keys iterator and index
for key in D.values():
    print(key)

print(list(D.items()))
for (key, value) in D.items():
    print(key, '=>', value) # Iterate over both keys and values
for both in T:
    a, b = both # Manual assignment equivalent
    print(a, b)
for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c) # Nested sequences work
for ((a, b), c) in [([1, 2], 3), ['XY', 6]]: print(a, b, c)
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:  # Used in for loop
    print(a, b, c)
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:print(a, b, c)


# Nested for loops  find same items
items = ["aaa", 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]
for key in tests: # For all keys
    for item in items:  # For all items
        if item == key:  # Check for match
            print(key, "was found")
            break
    else:
        print(key,"not found!")

for key in tests: # For all keys
    if key in items: # Let Python check for a match
        print(key, "was found")
    else:
        print(key, "not found!")
seq1 = "spam"
seq2 = "scam"
res = [] # Start empty
for x in seq1: # Scan first sequence
    if x in seq2: # Common item?
        res.append(x) # Add to result end
print(x)
[x for x in seq1 if x in seq2] # Let Python collect results

with open("test.txt","w") as file:
    file.write("hhhello, ming")
    file.write("I_like your cap")
    file.write("........")
file.close()
file = open('test.txt')
while True:
    line = file.readline() # Read line by line
    if not line: break
    print(line.rstrip()) # Line already has a \n

# to reverse a file’s lines
for line in reversed([open('test.txt').readlines()]): print(list(line))
# Python code to demonstrate working of
# reversed()

# For string
seqString = 'geeks'
print(list(reversed(seqString)))

# For tuple
seqTuple = ('g', 'e', 'e', 'k', 's')
print(list(reversed(seqTuple)))

# For range
seqRange = range(1, 5)
print(list(reversed(seqRange)))

# For list
seqList = [1, 2, 4, 3, 5]
print(list(reversed(seqList)))

# ord()
# Given a string of length one, return an integer representing the Unicode code
# point of the character when the argument is a unicode object,
# or the value of the byte when the argument is an 8-bit string.
value = ord("A")
value2 = ord("$")
print(value, value2)


# range(a,b,c)  a to b-1 by c
print(list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))
for i in range(3):print(i, 'Pythons')


#Sequence Scans: while and range Versus for
i = 0
X= "spam"
while i < len(X): # while loop iteration
    print(X[i], end=' ')
    i += 1
for i in range(len(X)): print(X[i], end=' ') # Manual range/len iteration
for item in X: print(item, end=' ') # Use simple iteration if you can

S = 'spam'
for i in range(len(S)): # For repeat counts 0..3
     S = S[1:] + S[:1] # Move front item to end
     print(S, end=' ')
S = 'abcdefghijk'
for c in S[::2]: print(c, end=' ')


L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 1
print(L)


#Parallel Traversals: zip and map
# built-in zip function allows us to use for loops to visit multiple sequences
# in parallel—not overlapping in time, but during the same loop.
L1 = [1,2,3,4]
L2 = [5,6,7,8]
print(zip(L1, L2))
print(list(zip(L1, L2)))
for (x, y) in zip(L1, L2):print(x, y, '--', x+y)
T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)
print(list(zip(T1, T2, T3)))

S1 = 'abc'
S2 = 'xyz123'
print(list(zip(S1, S2)))  # only first 3 items are linked

print(list(map(ord, 'spam')))
res = []
for c in 'spam': res.append(ord(c))
print(res)

keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
print(list(zip(keys, vals)))
D2 = {}
for (k, v) in zip(keys, vals): D2[k] = v  # creat a dic
print(D2)
{k: v for (k, v) in zip(keys, vals)}  # another way



# Generating Both Offsets and Items: enumerate
S = 'spam'
offset = 0
for item in S:
    print(item, 'appears at offset', offset)
    offset += 1

# enumerate!!!
S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)
E = enumerate(S)
print(next(E))
print(next(E))
print(next(E))

[c * i for (i, c) in enumerate(S)]
for (i, l) in enumerate(open('test.txt')):print('%s) %s' % (i, l.rstrip()))
