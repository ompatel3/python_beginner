# Learning python 5e page  687
# CHAPTER 25
# Advanced Module Topics

from unders import *  # if you use * which means you can Load non _X names only
print(a, c)
import unders  # * you can Load _X names
print(unders._b)
from alls import *  # Load __all__ names only
print(a, _c)
# print(d)  wrong

from alls import a, b, _c, _d
print(a, b, _c, _d)

import alls
print(a, b, _c, _d)
print(alls.a, alls.b, alls._c, alls._d)

import runme
runme.tester()


# Unit Tests with __name__
import minmax
import minmax2
print(minmax2.minmax(minmax2.lessthan, 's', 'p', 'a', 'a'))

# The as Extension for import and from
# import modulename as name

# Learning python 5e page  783
# CHAPTER 26
# Advanced Module Topics
# OOP: The Big Picture
# OOP story in Python boils down to this expression: object.attribute

class FirstClass: # Define a class object
    def setdata(self, value):# Define class's methods, self is the class defined
        self.data = value
    def display(self):
        print(self.data)  # self.data: per instance
x = FirstClass()  # define x and y both are class
y = FirstClass()
x.setdata("King Arthur")  # set value by using class fun setdata
y.setdata(3.14159)
x.display()  # display value by using class fun setdata
y.display()
x.anothername = "spam"  # Can set new attributes here too!
# This would attach a new attribute called anothername, which may or may not be used
# by any of the class’s methods, to the instance object x.

class SecondClass(FirstClass):  # Inherits setdata (all attr. in Firstclass can be used in Second Class)
    def __init__(self, value): # On "ThirdClass(value)" so that we can add value in the thirdclass
        self.data = value
    def display(self):
        print('Current value = "%s"' % self.data)
z = SecondClass("1234") # define z same as x
print(z) # we do not define __str__ so that it cannot be printed as 1234
z.display()
z.setdata(42)
z.display()
x.display()

# Classes Are Attributes in Modules
# from modulename import FirstClass # Copy name into my scope
# class SecondClass(FirstClass): # Use class name directly
# def display(self): ...


# __init__
# __init__ is run when a new instance object is created: self is the new ThirdClass
# __add__
# __add__ is run when a ThirdClass instance appears in a + expression.
# __str__ is run when an object is printed (technically, when it’s converted to its
# print string by the str built-in function or its Python internals equivalent).

class ThirdClass(SecondClass): # Inherit from SecondClass
    def __init__(self, value): # On "ThirdClass(value)" so that we can add value in the thirdclass
        self.data = value
    def __add__(self, other): # On "self + other"
        return ThirdClass(self.data + other)
    def __str__(self): # On "print(self)", "str()"
        return '[ThirdClass: %s]' % self.data
    def mul(self, other):  # In-place change: named
        self.data *= other

a = ThirdClass('abc') # init called
a.display()
print(a)
b = a + 'xyz'  # b is also a class here
b.display()
print(b)
a.mul(3)
print(a)
a.display()
b.mul(4)
print(b)


# Simplest Python Class
class rec: pass # Empty namespace object
rec.name = 'Bob' # Just objects with attributes
rec.age = 40
print(rec.name)
x = rec() # assign class to x and y
y = rec()
print(x.name, y.name)

x.name = 'Sue' # change x class
print(rec.name, x.name, y.name)

# the __dict__ attribute is the namespace dictionary for most class-based bjects.
print(list(rec.__dict__.keys()))
print(list(name for name in rec.__dict__ if not name.startswith('__')))  # what we defined
print(x.name, x.__dict__['name'])
# print(x.__dict__['age']) # Indexing dict does not do inheritance
# an attribute can often be fetched by either dictionary indexing(x.__dict__['name']) or attribute notation(x.name)

# created completely independently of any class object
def uppername(obj):
   return obj.name.upper() # Still needs a self argument (obj)
print(uppername(x))
rec.method = uppername
print(y.method())


# Records Revisited: Classes Versus Dictionaries
rec = ('Bob', 40.5, ['dev', 'mgr']) # Tuple-based record
print(rec[0])


rec = {}  # Dictionary-based record
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['jobs'] = ['dev', 'mgr']
print(rec['name'])


class rec: pass
rec.name = 'Bob' # Class-based record
rec.age = 40.5
rec.jobs = ['dev', 'mgr']

print(rec.name)
a = rec()
print(a.jobs)

class rec: pass
pers1 = rec() # Instance-based records
pers1.name = 'Bob'
pers1.jobs = ['dev', 'mgr']
pers1.age = 40.5

pers2 = rec()
pers2.name = 'Sue'
pers2.jobs = ['dev', 'cto']

print(pers1.name, pers2.name)

class Person:
    def __init__(self, name, jobs, age=None): # method
        self.name = name
        self.jobs = jobs
        self.age = age
    def info(self): # attr.
        return (self.name, self.jobs)

rec1 = Person('Bob', ['dev', 'mgr'], 40.5) # Construction calls
rec2 = Person('Sue', ['dev', 'cto'])

print(rec1.jobs, rec2.info()) # Attributes + methods
