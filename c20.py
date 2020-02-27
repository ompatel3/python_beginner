# Learning python 5e page 415
# CHAPTER 14 Iterations and Comprehensions

# iterations
for x in [1, 2, 3, 4]: print(x ** 2, end=' ')
for x in (1, 2, 3, 4): print(x ** 3, end=' ')

#The Iteration Protocol: File Iterators
# iterator : iter function
L = [1, 2, 3]
I = iter(L) # Obtain an iterator object from an iterable
print(I)
print(I.__next__()) # Call iterator's next to advance to next item
print(I.__next__())
print(I.__next__())

with open('script2.py','w') as f:
    f.write('import sys\nprint(sys.path)\nx = 2\nprint(x ** 32)\n')
print(open('script2.py').read())
f = open('script2.py')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
# next
f = open('script2.py')
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

# line.upper
for line in open('script2.py'):print(line.upper(), end='')


# read a file line by line with a while loop
f = open('script2.py')
while True:
    line = f.readline()
    if not line: break
    print(line.upper(), end='')

f = open('script2.py')
print(iter(f).__next__())
print(iter(f) is f)
print(iter(f) is f.__iter__())


# Manual iteration
L = [1, 2, 3]
I = iter(L)
while True:
    try:
        X = next(I) # X = I.__next__()
    except StopIteration:
        break
    print(X ** 2, end=" ")

# Other Built-in Type Iterables
D = {'a':1, 'b':2, 'c':3}
for key in D.keys():
    print(key, D[key])
for key in D: print(key, D[key])
I = iter(D)
print(next(I))
print(next(I))
print(next(I))
# os.popen (a tool for reading the output of shell commands)
import os
P = os.popen('dir')
print(P.__next__())
print(P.__next__())
I = iter(P)
print(next(I))
print(I.__next__())
R = range(5)
print(R)
I = iter(R)
print(next(I))
print(next(I))


E = enumerate('spam')
I = iter(E)
print(next(I))
print(next(I))
print(list(enumerate('spam')))

Z = zip((1, 2, 3), (10, 11, 12))
I1 = iter(Z)
I2 = iter(Z)
print(next(I1))
print(next(I1))
print(next(I2))

R = range(3)
I1, I2 = iter(R), iter(R)
print([next(I1), next(I1), next(I1)])

R = range(10)
I = iter(R)
print(next(I))
print(I.__next__())
print(I.__next__())
print(I.__next__())

# The Documentation Interlude

import sys
print(dir(sys))
len(dir(sys))
len([x for x in dir(sys) if not x.startswith('__')]) # Non __X names only
len([x for x in dir(sys) if not x[0] == '_']) # Non underscore names only

# see list and string attributes
len(dir([])), len([x for x in dir([]) if not x.startswith('__')])
len(dir('')), len([x for x in dir('') if not x.startswith('__')])
print(dir(str) == dir(''))
print(dir(list) == dir([]))
spam = 40
def square(x):
    """
    function documentation
    can we have your liver then?
    """
    return x ** 2 # square
class Employee:
    "class documentation"
    pass
print(square(4))
print(square.__doc__)
#The whole point of this documentation protocol is that your comments are retained
# for inspection in __doc__ attributes after the file is imported
import sys
print(sys.__doc__)
print(int.__doc__)
print(map.__doc__)


# PyDoc: The help Function
import sys
help(sys.getrefcount)
print(help(sys))
print(help(dict))
print(help(str.replace))