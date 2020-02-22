# Learning python 5e page 175 to 204
# chapter 6 The Dynamic Typing Interlude
# Variable creation
# Variable types
# Variable use
# Names - reference - objects(have different types) ===> variables
# In sum, variables are created when assigned, can reference any type of object,
# and must be assigned before they are referenced.
# Names have no types; as stated earlier, types live with objects, not names
# we actually made the variable reference a different type of object
# types are associated with objects in Python, not with variables
# Names and objects after running the assignment a = 3.
# a becomes a reference to the object 3.

a = 3
b = a
a = 'spam'
print(a)
print(b)
L1 = [2, 3, 4]
L2 = L1  # same reference with L1
L1[0] = 24
print(L1)
print(L2)

L1 = [2, 3, 4]
L2 = L1[:]  # copy the content of L1
L1[0] = 24
print(L1)
print(L2)

import copy
Y = [2, 3, 4]
X = copy.copy(Y) # Make top-level "shallow" copy of any object Y
X = copy.deepcopy(Y) # Make deep copy of any object Y: copy all nested parts

L = [1, 2, 3]
M = L # M and L reference the same object
print(L == M) # Same values
print(L is M) # Same objects

L = [1, 2, 3]
M = [1, 2, 3] # M and L reference different objects!!!
print(L == M) # Same values
print(L is M) # Different objects

X = 42
Y = 42 # Should be two different objects
print(X == Y)
print(X is Y)  # Same object anyhow: caching at work!

X = "s" # string?
Y = "s"
print(X == Y)
print(X is Y)  # Same object anyhow: caching at work!

# Because small integers and strings are cached and reused,
# though, is tells us they reference the same single object.


#ask Python how many references there are to an object:
import sys
print(sys.getrefcount(1)) # 106 pointers to this shared piece of memory
#When I ask about the integer object 1 in the PyCharm GUI, it reports 106 reuses of this same object
A = ["spam"]
B = A
B.append("shrubbery")
print(A)
print(B)

A = "spam"
B = A
B = "shrubbery"
print(A)
print(B)


# String Fundamentals
# 3 types of string： unicode， bytes， bytearray
# 2 types of file: text, binary
# From a functional perspective, strings can be used to represent just about anything that
# can be encoded as text or bytes



# common string literals and operations
S = '' # Empty string
print(S)
S = "spam's"  #Double quotes, same as single
print(S)
S = 's\np\ta\x00m' # Escape sequences \n = tab, \t white space, \x0 :Null: binary 0 character (doesn’t end string)
print(S)
S = """...multiline...""" # Triple-quoted block strings
print(S)
S = r'\temp\spam' # read Raw strings (no escapes)
print(S)
B = b'sp\xc4m' # Byte strings
print(S)
U = u'sp\u00c4m' #  Unicode strings
print(S)
print(S*1 + S*2)  # Concatenate, repeat
S = "abcdefg"
print(S[1], S[2:5], len(S)) # Index, slice, length
# "a {0} parrot".format(kind)  String formatting
S.find('ab') # String methods search
# S.rstrip() # remove whitespace
# S.replace('pa', 'xx')  replacement
# S.split(',') split on delimiter
# S.isdigit() content test
# S.lower() case conversion
# S.endswith('spam') end test
# 'spam'.join(strlist) delimiter join
# S.encode('latin-1') Unicode encoding
# B.decode('utf8') Unicode decoding
# for x in S: print(x), 'spam' in S,  Iteration, membership
# [c * 2 for c in S], map(ord, S), re.match('sp(.*)am', line) Pattern matching: library module




#Single- and Double-Quoted Strings Are the Same
print('shrubbery', "shrubbery")
title = "Meaning " 'of' " Life"
print(title)
# Adding commas between these strings would result in a tuple, not a string
print('knight\'s', "knight\"s")
# you can also embed quote characters by escaping them with backslashes



# Escape Sequences Represent Special Characters
s = 'a\nb\tc'
print(s)

# escape
# \newline  Ignored (continuation line)
# \\ Backslash (stores one \)
# \' Single quote (stores ')
# \" Double quote (stores ")
# \a Bell
# \b Backspace
# \f Formfeed
# \n Newline (linefeed)
# \r Carriage return
# \t Horizontal tab
# \v Vertical tab
# \xhh Character with hex value hh (exactly 2 digits)
# \ooo Character with octal value ooo (up to 3 digits)
# \0 Null: binary 0 character (doesn’t end string)
# \N{ id } Unicode database ID
# \uhhhh Unicode character with 16-bit hex value
# \Uhhhhhhhh Unicode character with 32-bit hex valuea
# \other Not an escape (keeps both \ and other)
s = 'a\0b\0c'
print(s)
print(len(s)) # here’s a five-character string that embeds two characters with binary zero values
s = '\001\002\x03'
print(s)
print(len(s))
s = "s\tp\na\x00m"
print(s)
print(len(s)) #contains the characters “spam”, a tab and
# newline, and an absolute zero value character coded in hex:
s = "C:\py\code"
print(s)
print(len(s))
# To code literal backslashes explicitly such that they are retained in your strings, double
# them up (\\ is an escape for one \) or use raw strings
# myfile = open('C:\\new\\text.dat', 'w') or
# myfile = open(r'C:\new\text.dat', 'w')

# triple quotes
# it is a syntactic convenience for coding multiline text data
mantra = """Always look
... on the bright
... side of life."""
print(mantra)

menu = """spam # comments here added to string!
... eggs # ditto
... """
print(menu)


#Basic string Operations
len('abc') # Length: number of items
'abc' + 'def' # Concatenation: a new string
'Ni!' * 4 # Repetition: like "Ni!" + "Ni!" + ...
print('------- ...more... ---') # 80 dashes, the hard way
print('-' * 80) # 80 dashes, the easy way
myjob = "hacker"
for c in myjob: print(c, end=' ') # Step through items, print each
print("k" in myjob)  # Found
print("z" in myjob)  #Not found
print('spam' in 'abcspamdef')  # Substring search, no position returned


# Indexing and Slicing
S = 'spam'
S[0], S[-2]  # Indexing from front or end
S[1:3], S[1:], S[:-1] # Slicing: extract a section
# Indexing (S[i]) fetches components at offsets:
# The first item is at offset 0.
# Negative indexes mean to count backward from the end or right.
# S[0] fetches the first item.
# S[−2] fetches the second item from the end (like S[len(S)−2]).

# Slicing (S[i:j]) extracts contiguous sections of sequences:
# The upper bound is noninclusive.
# Slice boundaries default to 0 and the sequence length, if omitted.
# S[1:3] fetches items at offsets 1 up to but not including 3.
# S[1:] fetches items at offset 1 through the end (the sequence length).
# S[:3] fetches items at offset 0 up to but not including 3.
# S[:−1] fetches items at offset 0 up to but not including the last item.
# S[:] fetches items at offsets 0 through the end—making a top-level copy of S.

# Extended slicing (S[i:j:k]) accepts a step (or stride) k, which defaults to +1:
# Allows for skipping items and reversing order—see the next section.
S = 'abcdefghijklmnop'
print(S[1:10:2])  # Skipping items by 2
print(S[::2])
print("hello"[::-1])
print('abcedfg'[5:1:-1])
'spam'[slice(1, 3)] # same as'spam'[1:3]
'spam'[slice(None, None, -1)] # same as 'spam'[::-1]
