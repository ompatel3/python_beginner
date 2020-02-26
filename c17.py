# # Learning python 5e page 319
# # chapter 10 Python Statements
# # if
#
# # if x > y:
# #     x = 1
# #     y = 2
# # if (A == 1 and
# #     B == 2 and
# #     C == 3):
# #         print('spam' * 3)
#
# ## input !!!
# while True:
#     reply = input('Enter text:')
#     if reply == 'stop': break  # break the while loop
#     print(int(reply) ** 2)
# print('Bye')
#
# S = '123'
# T = 'xxx'
# print(S.isdigit(), T.isdigit())
# while True:
#     reply = input('Enter text:')
#     if reply == 'stop': break
#     elif not reply.isdigit():
#         print('Bad!' * 8)
#     else:
#         print(int(reply) ** 2)
# print('Bye')
#
# # use try, except
# while True:
#     reply = input('Enter text:')
#     if reply == 'stop': break
#     try:
#         num = int(reply)
#     except:
#         print('Bad!' * 8)
#     else:
#         print(num ** 2)
# print('Bye')
#
# # more simple
# while True:
#     reply = input('Enter text:')
#     if reply == 'stop': break
#     try:
#         print(float(reply) ** 2)
#     except:
#         print('Bad!' * 8)
# print('Bye')
#
# # Nesting Code Three Levels Deep
# while True:
#     reply = input('Enter text:')
#     if reply == 'stop':break
#     elif not reply.isdigit():
#         print('Bad!' * 8)
#     else:
#         num = int(reply)
#         if num < 20:
#             print('low')
#         else:
#             print(num ** 2)
# print('Bye')


#Sequence Assignments
nudge = 1
wink = 2
A, B = nudge, wink # Tuple assignmen
[C, D] = [nudge, wink] # List assignment
print(A,B,C,D)
nudge, wink = wink, nudge # Tuples: swaps values
print(nudge, wink)
[a, b, c] = (1, 2, 3) # Assign tuple of values to list of names
print(a,c)
(a, b, c) = "ABC" # Assign string of characters to tuple
print(a,c)
string = 'SPAM'
a, b, c, d = string # Same number on both sides
print(a, d)
a, b, c = string[0], string[1], string[2:] # Index and slice
print(a,b,c)
a, b = string[:2] # Same, but simpler
print(a, b)
(a, b), c = string[:2], string[2:] # Nested sequences
print(a)
((a, b), c) = ('SP', 'AM') # Paired by shape and position
print(a, b, c)
# for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: ... # Simple tuple assignment
# for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: ... # Nested tuple assignment
red, green, blue = range(3)
print(blue)
L = [1, 2, 3, 4]
while L: # each ele in L
    front, L = L[0], L[1:]
    print(front, L)
seq = [1, 2, 3, 4]
a, b, c, d = seq
print(a, b, c, d)
print(a,d)
a, *b = seq  # * means rest
print(b)
a, *b = 'spam'
print(b)  # not "pam"
a, b = seq[:-1], seq[-1]
print(a)

L = [1, 2, 3, 4]
while L:
    front, *L = L # Get first, rest without slicing
    print(front, L)
for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    a, b, c = all[0], all[1:3], all[3]
    print(a,b,c)

# Multiple-Target Assignments
a = b = c = 'spam'
print(a,b,c)
a = b = []
b.append(42)
print(a,b)
S = "spam"
S += "SPAM"
print(S)


# function and expression
x = print('spam')
print(x)

# Expression Statements and In-Place Changes
L = [1, 2]
L.append(3)
print(L)

L = L.append(4)
print(L)  # So we lose our list!


# print!!
x = 'spam'
y = 99
z = ['eggs']
print(x, y, z)
print(x, y, z, sep='') # Suppress separator
print(x, y, z, sep=', ') # Custom separator
print(x, y, z, end='') # Suppress line break
print(x, y, z, end=''); print(x, y, z) # Two prints, same output line
print(x, y, z, end='...\n') # Custom line end
print(x, y, z, sep='...', end='!\n') # Multiple keywords
print(x, y, z, end='!\n', sep='...') # Order doesn't matter
print(x, y, z, sep='...', file=open('data.txt', 'w')) # Print to a file
print(open('data.txt').read())
text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
print(text)

import sys # Printing the hard way
sys.stdout.write('hello world\n')

X = 1; Y = 2
open('temp2', 'w').write(str(X) + ' ' + str(Y) + '\n')
print(open('temp2', 'r').read())

# if
# if test1: # if test
#     statements1 # Associated block
# elif test2: # Optional elifs
#     statements2
# else: # Optional else
#     statements3

x = 'killer rabbit'
if x == 'roger':
    print("shave and a haircut")
elif x == 'bugs':
    print("what's up doc?")
else:
    print('Run away! Run away!')
branch = {'spam': 1.25,'ham': 1.99,'eggs': 0.99}
print(branch.get('spa', 'Bad choice'))
print(branch.get('spam', 'Bad choice'))

try:
    print(branch["spam"])
except KeyError:
    print('Bad choice')


if a == b and c == d and \
d == e and f == g:
    print('olde') # Backslashes allow continuations...
if (a == b and c == d and
d == e and e == f):
    print('new') # But parentheses usually do too, and are obvious

# boolen test
# X and Y
# Is true if both X and Y are true
# X or Y
# Is true if either X or Y is true
# not X
# Is true if X is false (the expression returns True or False)

A = 't' if 'spam' else 'f'
print(A)
A = 't' if "" else 'g'
print(A)
print(['f', 't'][bool('')])
print(['f', 't'][bool('spam')])

print(bool(''))
print(bool('spam'))