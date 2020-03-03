# build a distribution
# step1 Begin by creating a folder for your module
# step2 Create a file called “setup.py” in your new folder.
# like from distutils.core import setup
# setup(
# name = 'nester',
# version = '1.0.0',
# py_modules = ['nester'],
# author = 'hfpython',
# author_email = 'hfpython@headfirstlabs.com',
# url = 'http://www.headfirstlabs.com',
# description = 'A simple printer of nested lists',
# )
# step3 Build a distribution file.
# Open a terminal window within your folder and type a single command: E:\pythonwork\python.exe setup.py sdist.(your python path)
# step4 Install your distribution into your local copy of Python: E:\pythonwork\python.exe setup.py install.


# import yout module
import nester
cast = ['Palin', 'Cleese', 'Idle', 'Jones', 'Gilliam', 'Chapman']
nester.print_lol(cast)

# Built-in functions (BIF)
# range
for num in range(4):
    print(num)
# list
aTuple = (123, 'xyz', 'zara', 'abc')
print(aTuple)
aList = list(aTuple)
print ("List elements : ", aList)
# enumerate
l1 = ["eat","sleep","repeat"]
s1 = "geek"
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print("Return type:",type(obj1))
print(list(enumerate(l1)))
print(list(enumerate(s1,2)))
# printing the tuples in object directly
for ele in enumerate(l1):
    print(ele)
print
# changing index and printing separately
for count,ele in enumerate(l1,100):
    print(count,ele)
# int() Converts a string or another number to an integer (if possible).
num = 13
String = '187'
result_1 = int(String) + num
print("int('187') + 13 = ", result_1)
# convert binary/quanternary num to decimal num
str = '100'
print("int('100') with base 2 = ", int(str, 2))
print("int('100') with base 4 = ", int(str, 4))
print("int('100') with base 8 = ", int(str, 8))
print("int('100') with base 16 = ", int(str, 16))
# id()Returns the unique identification for a Python data object.
print('id of 5 =',id(5))
a = 5
print('id of a =',id(a))
c = 5.0
print('id of c =',id(c))
#next()
random = [5, 9, 'cat']
# converting list to iterator
randomIterator = iter(random)
print(randomIterator)
# Output: 5
print(next(randomIterator))

# Output: 9
print(next(randomIterator))

# Output: 'cat'
print(next(randomIterator))
random = [5, 9]

# converting list to iterator
randomIterator = iter(random)

# Output: 5
print(next(randomIterator, '-1'))

# Output: 9
print(next(randomIterator, '-1'))

# randomIterator is exhausted
# Output: '-1'
print(next(randomIterator, '-1'))
print(next(randomIterator, '-1'))
print(next(randomIterator, '-1'))

# creat a BIF
def print_lol(the_list, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item,level+1)
        else:
            for tab_stop in range(level):
              print("\t",end="")
            print(each_item)
movies = [ "The Holy Grail", 1975, "Terry Jones & Terry Gilliam",91,["Graham Chapman", ["Michael Palin",
"John Cleese", "Terry Gilliam", "Eric Idle","Terry Jones"]]]
print_lol(movies,0)
# the difference between the print ("\t",end="") and  print("\t")
print("\t",end="")
print("A")
print("\t")
print("A")
#examples
names = ['John', 'Eric', ['Cleese', 'Idle'], 'Michael', ['Palin']]
print_lol(names)

# more complex BIF
def print_lol2(the_list, indent=False, level=0):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol2(each_item,indent, level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='')
            print(each_item)
print_lol2(names)
print_lol2(names,True,level=1)
