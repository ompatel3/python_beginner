# Learning python 5e page  860
# CHAPTER 29
# Class Coding Details


class SharedData:
    spam = 42  # Generates a class data attribute
x = SharedData() # Make two instances
y = SharedData()
print(x.spam, y.spam)
SharedData.spam = 99  # change in class
print(x.spam, y.spam, SharedData.spam)
x.spam = 88 # change through through an instance
print(x.spam, y.spam, SharedData.spam)

class MixedNames: # Define class
    data = 'spam'  # Assign class attr
    def __init__(self, value):  # Assign method name
        self.data = value  # Assign instance attr

    def display(self):
        print(self.data, MixedNames.data)  # Instance attr, class attr

x = MixedNames(1)
y = MixedNames(2) # Each has its own data
x.display(), y.display()

# Methods
class NextClass: # Define class
    def printer(self, text): # Define method
        self.message = text # Change instance
        print(self.message) # Access instance
x = NextClass()
x.printer('instance call')
print(x.message)
NextClass.printer(x, 'class call')
print(x.message)

# Specializing Inherited Methods
class Super:
    def method(self):
        print('in Super.method')
class Sub(Super):
    def method(self):  # Override method
        print('starting Sub.method')  # Add actions here
        Super.method(self)  # Run default action
        print('ending Sub.method')
x = Super()
x.method()
x = Sub()
x.method()

class Super:
    def method(self):
        print('in Super.method')  # Default behavior

    def delegate(self):
        self.action()  # Expected to be defined

class Inheritor(Super):  # Inherit method verbatim
    pass

class Replacer(Super):  # Replace method completely
    def method(self):
        print('in Replacer.method')

class Extender(Super):  # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):  # Fill in a required method
    def action(self):
        print('in Provider.action')
if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()

# Abstract Superclasses
# assert scheme in action
class Super:
    def delegate(self):
        self.action()

    def action(self):
        print('action must be defined!') # If this version is called
X = Super()
X.delegate()
class Super:
    def delegate(self):
        self.action()

    # def action(self):
    #     assert False 'action must be defined!' # If this version is called
# other raise error
class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('action must be defined!')

X=Super()
# X.delegate()


X = 11 # Global in module
def g1():
    print(X) # Reference global in module (11)
def g2():
    global X
    X = 22 # Change global in module
def h1():
    X = 33 # Local in function
    def nested():
        print(X) # Reference local in enclosing scope (33)
def h2():
    X = 33 # Local in function
    def nested():
        nonlocal X # Python 3.X statement
        X = 44 # Change local in enclosing scope

def classtree(cls, indent):
    print('.' * indent + cls.__name__) # Print class name here
    for supercls in cls.__bases__: # Recur to all superclasses
        classtree(supercls, indent+3) # May visit super > once
def instancetree(inst):
    print('Tree of %s' % inst) # Show instance
    classtree(inst.__class__, 3) # Climb to its class

def selftest():
    class A: pass

    class B(A): pass

    class C(A): pass

    class D(B, C): pass

    class E: pass

    class F(D, E): pass

    instancetree(B())
    instancetree(F())
if __name__ == '__main__': selftest()
