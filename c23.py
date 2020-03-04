# Learning python 5e page 554-581
# CHAPTER 19 Advanced Function Topics



# Summation with Recursion
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

print(mysum([1, 2, 3, 4, 5]))

# Coding Alternatives
def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:]) # Use ternary expression
def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])
def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)
print(mysum(('s', 'p', 'a', 'm')))

def mysum(L):
    if not L: return 0
    return nonempty(L) # Call a function that calls me
def nonempty(L):
    return L[0] + mysum(L[1:]) # Indirectly recursive

# Loop Statements Versus Recursion

L = [1, 2, 3, 4, 5]
sum = 0
while L:
    sum += L[0]
    L = L[1:]

L = [1, 2, 3, 4, 5]
sum = 0
for x in L: sum += x
print(sum)


# problem using recursion to sum [1, [2, [3, 4], 5], 6, [7, 8]]
L = [1, [2, [3, 4], 5], 6, [7, 8]]
def nestsum(A):
    res = 0
    for ele in A:
        if isinstance(ele, list):
            res += nestsum(ele)
        else: res += ele
    return res
print(nestsum(L))

# Recursion versus queues and stacks
#  add nested in end of list
def sumtree(L): # Breadth-first, explicit queue
    tot = 0
    items = list(L) # Start with copy of top level
    while items:
        front = items.pop(0) # Fetch/delete front item
        if not isinstance(front, list):
            tot += front # Add numbers directly
        else:
            items.extend(front) # <== Append all in nested list
    return tot

#  add nested in front of list
def sumtree(L): # Depth-first, explicit stack
    tot = 0
    items = list(L) # Start with copy of top level
    while items:
        front = items.pop(0) # Fetch/delete front item
        if not isinstance(front, list):
            tot += front # Add numbers directly
        else:
            items[:0] = front # <== Prepend all in nested list
    return tot

# Function Objects: Attributes and Annotations
def echo(message):
    print(message)
echo('Direct call')
x = echo  # Call object through name by adding ()
x('Indirect call!')

def indirect(func, arg):
    func(arg) # Pass the function to another function
indirect(echo, 'Argument call!')

schedule = [ (echo, 'Spam!'), (echo, 'Ham!') ] # Call functions embedded in containers by using turple
for (func, arg) in schedule: func(arg)


def make(label): # Make a function but don't call it
    def echo(message):
        print(label + ':' + message)
    return echo
make('Spam')("eggs!!!!!!!")


# Function Introspection
def func(a):
    b = 'spam'
    return b * a
print(func(8))
print(dir(func))

print(func.__code__.co_varnames)   # names of varibles in func
print(func.__code__.co_argcount)  # how many args in func
func.count = 0
func.count += 1
print(func.count)


# Function Annotations
def func(a, b, c):
    return a + b + c
print(func(1, 2, 3))

def func(a: 'spam', b: (1, 10), c:float) -> int:
    return a + b + c
print(func.__annotations__)

for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])

def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:  #set default
    return a + b + c

print(func())
print(func(1, c=10))
print(func.__annotations__)

# Anonymous Functions: lambda
# lambda argument1, argument2,... argumentN : expression using arguments
def func(x, y, z): return x + y + z
f = lambda x, y, z: x + y + z
print(func(4,8,11),f(4,8,11))
x = (lambda a="fee", b="fie", c="foe": print(a + b + c))
x("wee","duu")
def knights():
    title = 'Sir'
    action = (lambda x: print("title" + ' ' + x)) # Title in enclosing def scope
    return action # Return a function object

knights()("sb")

# lambda is also commonly used to code jump tables

L = [lambda x: x ** 2, # Inline function definition
lambda x: x ** 3,
lambda x: x ** 4] # A list of three callable functions

for f in L:
    print(f(2)) # Prints 4, 8, 16
    print(L[0](3)) # Prints 9
# OR use def
def f1(x): return x ** 2
def f2(x): return x ** 3 # Define named functions
def f3(x): return x ** 4
L = [f1, f2, f3] # Reference by name
for f in L:
    print(f(2)) # Prints 4, 8, 16
    print(L[0](3)) # Prints 9


# Multiway branch switches: The finale
# call function by dic
key = 'got'
{'already': (lambda: print(2 + 2)),'got': (lambda: print(2 * 4)),'one': (lambda: 2 ** 6)}[key]()
def f1(): return 2 + 2
def f2(): return 2 * 4
def f3(): print(2 ** 6)
key = 'one'
{'already': f1, 'got': f2, 'one': f3}[key]()


# How (Not) to Obfuscate Your Python Code
# X for i in list if True else Y
lower = (lambda x, y: print(x) if x < y else print(y))
lower('aa', 'bb')

import sys
showall = lambda x: list(map(sys.stdout.write, x))
t =showall(['spam\n', 'toast\n', 'eggs\n'])
print(t)
showall = lambda x: [sys.stdout.write(line) for line in x]
t = showall(('bright\n', 'side\n', 'of\n', 'life\n'))
print(t)
showall = lambda x: [print(line, end='') for line in x]
showall = lambda x: print(*x, sep='', end='')

# Scopes: lambdas Can Be Nested Too
def action(x):
    return (lambda y=1000: x + y)
act = action(99)
print(act())
# nested
((lambda x: (lambda y: print(x + y)))(99))(4)

# Mapping Functions over Iterables: map
counters = [1, 2, 3, 4]
updated = []
for x in counters:
    updated.append(x + 10)
print(updated)

def inc(x): print(x + 10) # Function to be run
list(map(inc, counters))
# list(map(func, range))     for i in range: func(i) and then make them a list
list(map((lambda x: print(x + 3)), counters))

# what happened in map function
def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res
[inc(x) for x in [1, 2, 3, 4]]

# Selecting Items in Iterables: filter
list(filter((lambda x: x > 0), range(-5, 5)))

# equivalent
res = []
for x in range(-5, 5):
    if x > 0:res.append(x)
print(res)

# equivalent
[x for x in range(-5, 5) if x > 0]


# Combining Items in Iterables: reduce
from functools import reduce
print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))
# equivalent
L = [1,2,3,4]
res = L[0]
for x in L[1:]: res = res + x
print(res)
reduce((lambda x, y: x * y), [1, 2, 3, 4])  # cumproduct

# what happened in reduce function
def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally

print(myreduce((lambda x, y: x * y), [1, 2, 3, 4, 5]))

import operator, functools
print(functools.reduce(operator.add, [2, 4, 6]))
# same
functools.reduce((lambda x, y: x + y), [2, 4, 6])