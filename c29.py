# Learning python 5e page  819
# CHAPTER 28
# A More Realistic Example
class Person:
    def __init__(self, name, job, pay): # Constructor takes three arguments
        self.name = name # Fill out fields when created
        self.job = job # self is the new instance object
        self.pay = pay


# set default
class Person:
    def __init__(self, name, job=None, pay=0): # Constructor takes three arguments
        self.name = name # Fill out fields when created
        self.job = job # self is the new instance object
        self.pay = pay

bob = Person('Bob Smith') # Test the class
sue = Person('Sue Jones', job='dev', pay=100000) # Runs __init__ automatically
print(bob.name, bob.pay) # Fetch attached attributes
print(sue.name, sue.pay) # sue's and bob's attrs differ


# second way to code
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
if __name__ == '__main__': # When run for testing only
# self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)

# Adding Behavior Methods

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.name.split()[-1]) # Extract object's last name
    sue.pay *= 1.10 # Give this object a raise
    print('%.2f' % sue.pay)

# Coding Methods
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self): # Behavior methods
        return self.name.split()[-1] # self is implied subject
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent)) # Must change here only
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(), sue.lastName()) # Use the new methods
    sue.giveRaise(.10) # instead of hardcoding
    print(sue.pay)
# Step 3: Operator Overloading
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self): # Added method
        return '[Person: %s, %s]' % (self.name, self.pay) # String to print
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)  # print changed by __repr__ method
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)

# Customizing Behavior by Subclassing
# bad
class Manager(Person): # Inherit Person attrs
    def giveRaise(self, percent, bonus=.10): # Redefine to customize
        self.pay = int(self.pay * (1 + percent + bonus))  # Bad: cut and paste

# good
class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus) # Good: augment original

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self): # Added method
        return '[Person: %s, %s]' % (self.name, self.pay) # String to print
class Manager(Person):
    def giveRaise(self, percent, bonus=.10):  # Redefine at this level
        Person.giveRaise(self, percent + bonus)  # Call Person's version
if __name__ == '__main__':
    bob = Person('Bob Smith')  # person module
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 'mgr', 50000)  # manager module Make a Manager: __init__
    tom.giveRaise(.10)  # Runs custom version
    print(tom.lastName())  # Runs inherited method
    print(tom)  # Runs inherited __repr__

# Step 5: Customizing Constructors, Too
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self): # Added method
        return '[Person: %s, %s]' % (self.name, self.pay) # String to print
class Manager(Person):
    def __init__(self, name, pay):  # Redefine constructor
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
if __name__ == '__main__':
    bob = Person('Bob Smith')  # person module
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)  # manager module Make a Manager: __init__
    tom.giveRaise(.10)  # Runs custom version
    print(tom.lastName())  # Runs inherited method
    print(tom)  # Runs inherited __repr__

# add department class
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self): # Added method
        return '[Person: %s, %s]' % (self.name, self.pay) # String to print
class Manager(Person):
    def __init__(self, name, pay):  # Redefine constructor
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):  # use
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 50000)
    development = Department(bob, sue)  # Embed objects in a composite
    development.addMember(tom)
    development.giveRaises(.10)  # Runs embedded objects' giveRaise
    development.showAll()  # Runs embedded objects' __repr__

# Special Class Attributes
bob = Person('Bob Smith')
print(bob)
print(bob.__class__)# Show bob's class and its name
print(bob.__class__.__name__)
print(list(bob.__dict__.keys()))  # Attributes are really dict keys
for key in bob.__dict__:
    print(key, '=>', bob.__dict__[key]) # Index manually
# getattr(name, key) ---- value
for key in bob.__dict__:
    print(key, '=>', getattr(bob, key)) # obj.attr, but attr is a var

# getattr
class AttrDisplay:
    """
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ",".join(attrs)
    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())
if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2
class SubTest(TopTest): pass
X, Y = TopTest(), SubTest()
print(X)
print(Y)


# Instance Versus Class Attributes
bob = Person('Bob Smith')
print(bob.__dict__.keys())
print(dir(bob))
print(list(name for name in dir(bob) if not name.startswith('__')))

# Classes’ Final Form

class Person(AttrDisplay):
    """
    Create and process person records
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):  # Assumes last is last
        return self.name.split()[-1]

    def giveRaise(self, percent):  # Percent must be 0..1
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    """
    A customized Person with special requirements
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)  # Job name is implied

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)

# Pickles and Shelves
bob = Person('Bob Smith') # Re-create objects to be stored
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

# store Person objects on a shelve database
import shelve
db = shelve.open('persondb') # Filename where objects are stored
for obj in (bob, sue, tom): # Use object's name attr as key
    db[obj.name] = obj # Store object on shelve by key
db.close() # Close after making changes

# Exploring Shelves Interactively
# glob module allows us to get directory listings in Python code to verify the files here
import glob
print(glob.glob('person*'))
print(open('persondb.dir').read())
# read in binary
print(open('persondb.dat','rb').read())

import shelve
db = shelve.open('persondb')  # reopen
len(db)  # Three 'records' stored
list(db.keys())
# Fetch bob by key
bob = db['Bob Smith'] # bob in class
print(bob)  # Runs __repr__ from AttrDisplay
bob.lastName()
for key in db: # Iterate, fetch, print
    print(key, '=>', db[key])
for key in sorted(db):
    print(key, '=>', db[key]) # Iterate by sorted keys


# Updating Objects on a Shelve
import shelve
db = shelve.open('persondb')  # Reopen shelve with same filename
for key in sorted(db): # Iterate to display database objects
    print(key, '\t=>', db[key]) # Prints with custom format
sue = db['Sue Jones'] # Index by key to fetch
sue.giveRaise(.10) # Update in memory using class's method
db['Sue Jones'] = sue # Assign to key to update in shelve
db.close()

# update
db = shelve.open('persondb')
for key in sorted(db):
    print(key, '=>', db[key])
db.close()
# update
db = shelve.open('persondb')
sue = db['Sue Jones'] # Index by key to fetch
sue.giveRaise(.10) # Update in memory using class's method
db['Sue Jones'] = sue # Assign to key to update in shelve
for key in sorted(db):
    print(key, '=>', db[key])
# update
db = shelve.open('persondb')
sue = db['Sue Jones'] # Index by key to fetch
sue.giveRaise(.10) # Update in memory using class's method
db['Sue Jones'] = sue # Assign to key to update in shelve
for key in sorted(db):
    print(key, '=>', db[key])
# ....

# Fetch object by key
import shelve
db = shelve.open('persondb')
rec = db['Sue Jones'] # Fetch object by key
print(rec)
print(rec.lastName())
print(rec.pay)

