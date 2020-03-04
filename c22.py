# Learning python 5e page 523-554
# CHAPTER 18 argument

def changer(a, b):
    a = 2
    b[0]="spam"
X = 1
L = [1, 2]
changer(X, L)  # Pass immutable and mutable objects
print(X)  # X did not change
print(L)

# because
X = 1
a = X # They share the same object
a = 2 # Resets 'a' only, 'X' is still 1
print(X)

# Simulating Output Parameters and Multiple Results
def multiple(x, y):
    x = 2  # Changes local names only
    y = [3, 4]
    return x, y
X = 4
L = [1, 2]
multiple(X, L)
print(X)
print(L)  # list changed
X, L = multiple(X, L) # Assign results to caller's names
print(X,L)


# Special Argument-Matching Modes

# easy match
def f(a, b, c): print(a, b, c)
f(1, 2, 3)
f(c=3, b=2, a=1) # set keywords
f(1, c=3, b=2)  # change position

# default
def f(a, b=2, c=3): print(a, b, c)
f(99) # Use defaults
f(1, c=6) # Choose defaults

# Combining keywords and defaults

def func(spam, eggs, toast=0, ham=0): # First 2 required
    print((spam, eggs, toast, ham))
func(toast=1, eggs=2, spam=3)


# headers
# Headers: Collecting arguments

def f(*args): print(args)   # tuple
f(2)
f(1, 2, 3, 4)

def f(**args): print(args) # dic
# f(1) wrong
f(a=1)

def f(a, *pargs, **kargs): print(a, pargs, kargs)
args = (1, 2)
args += (3, 4)
f(*args) # (1,2,3,4)?
f(1, 2, 3, x=1, y=2)

# Calls: Unpacking arguments
def func(a, b, c, d): print(a, b, c, d)
args = (1, 2)
args += (3, 4)
x = (1,9,88,1110)
y = [2,3,4,5]
# func(args) wrong!
func(*args)
func(*x)  # unpack turple
func(*y)  # unpack list
print(*x)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
func(*args) # get keys
func(**args)  # get values
func(*(1, 2), **{'d': 4, 'c': 3})
func(1, *(2,), c=3, **{'d':4})

# Applying functions generically

def tracer(func, *pargs, **kargs): # Accept arbitrary arguments
    print('calling:', func.__name__)
    return func(*pargs, **kargs)
def func(a, b, c, d):
    return a + b + c + d
print(tracer(func, 1, 2, c=3, d=4)) # 1,2---(1,2), c,d----dic, func---(1,2,3,4)

# Keyword-Only Arguments
# a may be passed by position or name again, but b and c must be keywords,
def kwonly(a, *, b=1, c):
    print(a, b, c)
kwonly(1, b=2, c=3)
kwonly(a=1, c=3)
# kwonly(a=1, c=3) kwonly() missing 1 required keyword-only argument: 'c'
def kwonly(a, *, b, c):print(a, b, c)
kwonly(1, c=3, b=2)
def kwonly(a, *, b='spam', c='ham'):print(a, b, c)
kwonly(1, c=3)
def kwonly(a, *, b, c='spam'):print(a, b, c)
# b has to be key
kwonly(1, b='eggs')

# Ordering rules
# 1.keyword-only arguments must be specified after a single star
# 2.not two named arguments cannot appear after the **args arbitrary keywords form
# eg.def kwonly(a, **, b, c):prrint(a,b,c)
# 3.** can’t appear by itself in the arguments list
# eg.def kwonly(**,args):print(args)
# Keyword-only cannot before **!
# eg.def f(a, *b, **d, c=6): print(a, b, c, d)
def f(a, *b, c=6, **d): print(a, b, c, d)
f(1, 2, 3, x=4, y=5)
f(1, 2, 3, x=4, y=5, c=7)
f(1, 2, 3, c=7, x=4, y=5)
def f(a, c=6, *b, **d): print(a, b, c, d) # c is not keyword-only here!
f(1, 2, 3, x=4)  # a-1,  c-2 default is 6, 3- ketword-only arg (3,), x=3--d
def f(a, *b, c=6, **d): print(a, b, c, d) # KW-only between * and **
f(1, *(2, 3), c=7, **dict(x=4, y=5)) # Unpack args at call  input: 1,2,3,c=7,4,5  1-a, (2,3)-b, 7-c default is 6, x,y---dic
f(1, *(2, 3), **dict(x=4, y=5, c=7)) # Keyword-only in **
f(1, c=7, *(2, 3), **dict(x=4, y=5)) # After or before *


# min function
def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res: res = arg
    return res

def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first

def min3(*args):
    tmp = list(args) # Or, in Python 2.4+: return sorted(args)[0]
    tmp.sort()
    return tmp[0]
print(min1(3, 4, 1, 2))
print(min2("bb", "aa"))
print(min3([2,2], [1,1], [3,3]))
# minmax
def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y # See also: lambda, eval
def grtrthan(x, y): return x > y

print(minmax(lessthan, 4, 2, 1, 5, 6, 3)) # Self-test code
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))



# Generalized Set Functions
def intersect(*args):
    res = []
    for x in args[0]: # Scan first sequence
        if x in res: continue # Skip duplicates
        for other in args[1:]: # For all other args
            if x not in other: break # Item in each one?
        else: # No: break out of loop
            res.append(x) # Yes: add items to end
    return res


def union(*args):
    res = []
    for x in args:
        for y in x:
            if not y in res:
                res.append(y)
    return res

s1, s2, s3 = "SPAM", "SCAM", "SLAM"
print(intersect(s1,s2,s3))
print(union(s1,s2,s3))

def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))

tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))
tester(intersect, ('ba', 'abcdefg', 'abdst', 'albmcnd'), False)


import sys
def print3(*args, **kargs):
    sep = kargs.get('sep', ' ') # Keyword arg defaults
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = str(args[0])
    first = True
    for arg in args[1:]:
        output += (sep if first else " ") + str(arg)
    first = False
    file.write(output + end)

print3(5,7 ,"dwidjjwi",111,"djw",888, sep='...', end='')

# Using Keyword-Only Arguments
def print3(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

print3(5,7,9,11, sep='...', end='')

# use dic.pop to return the value in dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
element = sales.pop('grapes')
print(element)


import sys
def print3(*args, **kargs):
    sep = kargs.pop('sep', ' ')
    end = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs: raise TypeError('extra keywords: %s' % kargs)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)
print3(5000,7000,9000,11000, sep='...', end='')

