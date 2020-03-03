# Learning python 5e page 475
# CHAPTER 16 Function Basics
# def name(arg1, arg2,... argN):
# ...
# return value


# times function


def times(x, y): # Create and assign function
    return x * y # Body executed when called

print(times(2,3))
print(times('Ni', 4))

# intersect function
def intersect(seq1, seq2):
    res = [] # Start empty
    for x in seq1: # Scan seq1
        if x in seq2: # Common item?
            res.append(x) # Add to end
    return res
s1 = "SPAM"
s2 = "SCAM"
print(intersect(s1, s2)) # Strings
print([x for x in s1 if x in s2])
print(intersect([1, 2, 3], (1, 4)))


# scope
X = 99
def func(Y):
    Z = X + Y # X is a global
    return Z
print(func(1))

X = 88 # Global X
def func():
    X = 99 # Local X: hides global, but we want this here
func()
print(X) # Prints 88: unchanged

#  there is no way to change a name outside a function without adding a global
# (or nonlocal) declaration to the def


X = 88 # Global X
def func():
    global X
    X = 99 # Global X: outside def
func()
print(X) # Prints 99

y, z = 1, 2 # Global variables in module
def all_global():
    global x # Declare globals assigned
    x = y + z # No need to declare y, z: LEGB rule

# Nested Scope Examples
X = 99 # Global scope name: not used
def f1():
    X = 88 # Enclosing def local
    def f2():
        print(X) # Reference made in nested def
    f2()

# print 88
f1() # Prints 88: enclosing def local
def f1():
    X = 88
    def f2():
        print(X) # Remembers X in enclosing def scope
    return f2 # Return f2 but don't call it
print(f1())
f1()()
action = f1() # Make, return function
action() # Call it now: prints 88


# Factory Functions: Closures
def maker(N):
    def action(X): # Make and return action
        return X ** N # action retains N from enclosing scope
    return action
f= maker(2)
print(f(3))
print(maker(10)(2))

# use lamada fucntions
def maker(N):
     return lambda X: X * N # lambda functions retain state too
print(maker(3)(4))

# Retaining Enclosing Scope State with Defaults.
def f1():
    x = 88
    def f2(x=3): # Remember enclosing scope X with defaults
        print(x)
    return f2
f1()()
f1()(19999)

#
def func():
    x = 4
    action = (lambda n: x ** n) # x remembered from enclosing def
    return action
print(func()(2))
f = func()
print(f(2))

def makeActions():
    acts = []
    for i in range(5): # Tries to remember each i
         acts.append(lambda x: i ** x) # But all remember same last i!
    return acts
print(makeActions())
print(makeActions()[1](2))
print(makeActions()[2](2))
print(makeActions()[3](2))

def makeActions():
    acts = []
    for i in range(5): # Use defaults instead
        acts.append(lambda x, i=i: i ** x) # Remember current i
    return acts
print(makeActions()[1](2))
print(makeActions()[2](2))
print(makeActions()[3](2))

def f1():
    x = 99
    def f2():
         def f3():
              print(x) # Found in f1's local scope!
         f3()
    f2()

f1()

# nonlocal in Action  to retain the state of varibles defined in nested def
def tester(start):
    state = start  # Referencing nonlocals works normally
    def nested(label):
        print(label, state)
    return nested
tester("you")("fuck")

# however it cannot work
# def tester(start):
#     state = start
#     def nested(label):
#         print(label, state)
#         state += 1 # Cannot change by default (never in 2.X)
#     return nested

def tester(start):
    state = start # Each call gets its own state
    def nested(label):
        nonlocal state # Remembers state in enclosing scope
        print(label, state)
        state += 1 # Allowed to change it if nonlocal
    return nested

tester(0)("fuck")

# Boundary cases
# nonlocals   vs   global
# first!!
# Nonlocals must already exist in enclosing def!
# wrong！！！！
# def tester(start):
#     def nested(label):
#         nonlocal state # Globals don't have to exist yet when declared
#         state = 0 # This creates the name in the module now
#         print(label, state)
#     return nested
# global does not need to exist in enclosing def!
# def tester(start):
#     def nested(label):
#         global state # Globals don't have to exist yet when declared
#         state = 0 # This creates the name in the module now
#         print(label, state)
#     return nested
# second
# nonlocals Must be in a def, not the module!
# spam = 99
# def tester():
#     def nested():
#         nonlocal spam # Must be in a def, not the module!
#         print('Current=', spam)
#         spam += 1
#     return nested

def tester(start):
    state = start # Each call gets its own state
    def nested(label):
        nonlocal state # Remembers state in enclosing scope
        print(label, state)
        state += 1 # Allowed to change it if nonlocal
        return nested

def tester(start):
    global state # Move it out to the module to change it
    state = start # global allows changes in module scope
    def nested(label):
         global state
         print(label, state)
         state += 1
    return nested
# State with Classes: Explicit Attributes (Preview)
class tester: # Class-based alternative (see Part VI)
    def __init__(self, start): # On object construction,
        self.state = start # save state explicitly in new object
    def nested(self, label):
        print(label, self.state) # Reference state explicitly
        self.state += 1 # Changes are always allowed
F = tester(0)
F.nested('spam')
F.nested('ham')

class tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label): # Intercept direct instance calls
        print(label, self.state) # So .nested() not required
        self.state += 1
H = tester(99)  # int input
H('juice')  # invokes__call
H('pancakes')

## nested.state!
def tester(start):
    def nested(label):
        print(label, nested.state) # nested is in enclosing scope
        nested.state += 1 # Change attr, not nested itself
    nested.state = start # Initial state after func defined
    return nested
F = tester(0)
F('spamddddd')

## string[0]
def tester(start):
    def nested(label):
        print(label, pp[0]) # Leverage in-place mutable change
        pp[0] += 1 # Extra syntax, deep magic?
        pp = [start]
    return nested
