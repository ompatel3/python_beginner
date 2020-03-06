# Learning python 5e page  620
# CHAPTER 20 Advanced Function Topics
# CHAPTER 21 The Benchmarking Interlude


def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs): # non-empty
         res.append(tuple(S.pop(0) for S in seqs))
    return res

def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs): # not all empty
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res
S1, S2 = 'abc', 'xyz123'
print(myzip(S1, S2))
print(all([[1, 2, 3], [2, 3, 4, 5]]))
print(all([[], [2, 3, 4, 5]]))

def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]
def mymapPad(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    index = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]
S1, S2 = 'abc', 'xyz123'
print(myzip(S1, S2))
print(mymapPad(S1, S2))
print(mymapPad(S1, S2, pad=99))

# generator
def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)
def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)

S1, S2 = 'abc', 'xyz123'
print(list(myzip(S1, S2)))
print(list(mymapPad(S1, S2)))
print(list(mymapPad(S1, S2, pad=99)))

# altenative
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]
def mymapPad(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    index = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]
S1, S2 = 'abc', 'xyz123'
print(myzip(S1, S2))
print(mymapPad(S1, S2))
print(mymapPad(S1, S2, pad=99))

# Comprehension Syntax Summary
[x * x for x in range(10)] # List comprehension: builds list
(x * x for x in range(10)) # Generator expression: produces items
{x * x for x in range(10)} # Set comprehension
{x: x * x for x in range(10)} # Dictionary comprehension


# Scopes and Comprehension Variables
print((X for X in range(5)))
[X for X in range(5)] #generator, set, dict, and list localize
Y = 99
for Y in range(5): pass # But loop statements do not localize names
print(Y)

X = 'aaa'
def func():
    Y = 'bbb'
    print(''.join(Z for Z in X + Y))  # Z comprehension, Y local, X global
func()

# Comprehending Set and Dictionary Comprehensions
{x * x for x in range(10)} # Comprehension
set(x * x for x in range(10)) # Generator and type name
{x: x * x for x in range(10)}
dict((x, x * x) for x in range(10))
# cannnot print(x)

res = set()
for x in range(10):
    res.add(x * x)
print(res)
res = {}
for x in range(10): # Dict comprehension equivalent
    res[x] = x * x
print(res)

# Extended Comprehension Syntax for Sets and Dictionaries
[x * x for x in range(10) if x % 2 == 0] # Lists are ordered
{x * x for x in range(10) if x % 2 == 0} # But sets are not
{x: x * x for x in range(10) if x % 2 == 0} # Neither are dict keys
print([x + y for x in [1, 2, 3] for y in [4, 5, 6]]) # Lists keep duplicates
print({x + y for x in [1, 2, 3] for y in [4, 5, 6]}) # But sets do not
print({x: y for x in [1, 2, 3] for y in [4, 5, 6]}) # Neither do dict keys
# for key - value, a key only have one value
print({x + y for x in 'ab' for y in 'cd'})
print({x + y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'})
print({k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'})
print({k.upper(): k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'})





# CHAPTER 21
# The Benchmarking Interlude


# Timing Module: Homegrown
from time import process_time
def timer(func, *args): # Simplistic timing function
    t1_start = process_time()
    for i in range(10000):
        func(*args)
    t1_stop = process_time()
    print("Elapsed time:", t1_stop, t1_start)
    print("Elapsed time during the whole program in seconds:", t1_stop - t1_start) # Total elapsed time in seconds
timer(pow, 2, 1000)
timer(str.upper, 'spam')

import timeit
print(min(timeit.repeat(number=10000, repeat=3, stmt="L = [1, 2, 3, 4, 5]\nfor i in range(len(L)): L[i] += 1")))
print(min(timeit.repeat(number=10000, repeat=3,stmt="L = [1, 2, 3, 4, 5]\ni=0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1")))

# Other Benchmarking Topics: pystones
def selector():
   global X # Force X to be global (everywhere)
   print(X)
   X = 88
selector()

X = 99
def selector():
    import __main__ # Import enclosing module
    print(__main__.X) # Qualify to get to global version of name
    X = 88 # Unqualified X classified as local
    print(X)
selector()

# Defaults and Mutable Objects
def saver(x=[]):
    x.append(1)
    print(x)
saver([2])
saver()# default
saver()# # Grows on each call!

def saver(x=None):
    if x is None:  # No argument passed?
        x = []  # Run code to make a new list each time
    x.append(1)
    print(x)
saver([2])
saver()
saver()  # Doesn't grow here

def saver():
    saver.x.append(1)
    print(saver.x)
saver.x = []
saver()
saver()
saver()

# Functions Without returns
def proc(x):
    print(x)  # No return is a None return
proc('testing 123...')
x = proc('testing 123...')
print(x)

list = [1, 2, 3]
b = list.append(4)
print(b)
print(list)
