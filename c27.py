# Learning python 5e page  669
# CHAPTER 22
# Modules: The Big Picture

import sys
print(sys.path)

# Module Creation
import module1
module1.printer('Hello world!')

from module1 import printer
printer('Hello world!')

from module1 import * # Copy out _all_ variables
printer('Hello world!')


import simple  # hello
print(simple.spam)
simple.spam = 2

import simple
print(simple.spam)  # Code wasn't rerun: attribute unchanged

from small import x, y
x = 42
y[0] = 42

import small
print(small.x)  # Small's x is not my x
print(small.y)  # But we share a changed mutable

# Cross-file name changes
from small import x, y
x = 42
import small
small.x = 42  # Changes x in other module
import small
print(small.x)  # Small's x is not my x
print(small.y)


# import and from Equivalence
# from module import name1, name2
# equivalent to
# import module # Fetch the module object
# name1 = module.name1 # Copy names out by assignment
# name2 = module.name2
# del module  # Get rid of the module name

# When import is required

# M.py
# def func():
# ...do something...

# N.py
# def func():
# ...do something else...

# O.py
# from M import func
# from N import func # This overwrites the one we fetched from M
# func() # Calls N.func only!

# O.py
# import M, N # Get the whole modules, not their names
# M.func() # We can call both names now
# N.func() # The module names make them unique

# Or
# O.py
# from M import func as mfunc # Rename uniquely with "as"
# from N import func as nfunc
# mfunc(); nfunc() # Calls one or the other


import module2
print(module2.sys)  #  built in module
print(module2.name) #  varibles
print(module2.func) #  function
print(module2.klass) # class
# Namespace Dictionaries
print(list(module2.__dict__.keys()))
# names created by author
print(list(name for name in module2.__dict__.keys() if not name.startswith('__')))
print(list(name for name in module2.__dict__ if not name.startswith('__')))
# return the value of keys
print(module2.name, module2.__dict__['name'])



# Attribute Name Qualification
import modb

# Namespace Nesting
import mod3
import mod2
import mod1

# reload Basics
# Unlike import and from:
# • reload is a function in Python, not a statement.
# • reload is passed an existing module object, not a new name.
# • reload lives in a module in Python 3.X and must be imported itself


# import module # Initial import
# ...use module.attributes...
# ... # Now, go change the module file
# ...
# from imp import reload # Get reload itself (in 3.X)
# reload(module1) # Get updated exports
# ...use module.attributes...


import changer
changer.printer()
# from imp import reload # bbefore 3.4
from importlib import reload
print(reload(changer))
changer.printer()