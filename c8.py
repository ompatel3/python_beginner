# effective python for beginners
# chapter 1 Pythonic Thinking
import os

# Item 1: Know Which Version of Python You’re Using
import sys
print(sys.version_info)
print(sys.version)

#Item 2: Follow the PEP 8 Style Guide
# PEP 8:Python Enhancement Proposal #8 is the style guide for how to format Python code
# 1. white space
# Use spaces instead of tabs for indentation.
# Use four spaces for each level of syntactically significant indenting.
# Lines should be 79 characters in length or less.
# Continuations of long expressions onto additional lines should be indented by four
# extra spaces from their normal indentation level.
# In a file, functions and classes should be separated by two blank lines.
# In a class, methods should be separated by one blank line.
# Don’t put spaces around list indexes, function calls, or keyword argument assignments.
# Put one—and only one—space before and after variable assignments.
# 2. Naming
# Functions, variables, and attributes should be in lowercase_underscore
# format.
# Protected instance attributes should be in _leading_underscore format.
# Private instance attributes should be in __double_leading_underscore
# format.
# Classes and exceptions should be in CapitalizedWord format.
# Module-level constants should be in ALL_CAPS format.
# Instance methods in classes should use self as the name of the first parameter
# (which refers to the object).
# Class methods should use cls as the name of the first parameter (which refers to
# the class).
# 3. Expressions and Statements
# Use inline negation (if a is not b) instead of negation of positive expressions
# (if not a is b).
# Don’t check for empty values (like [] or '') by checking the length (if
# len(somelist) == 0). Use if not somelist and assume empty values
# implicitly evaluate to False.
# The same thing goes for non-empty values (like [1] or 'hi'). The statement if
# somelist is implicitly True for non-empty values.
# Avoid single-line if statements, for and while loops, and except compound
# statements. Spread these over multiple lines for clarity.
# Always put import statements at the top of a file.
# Always use absolute names for modules when importing them, not names relative to
# the current module’s own path. For example, to import the foo module from the
# bar package, you should do from bar import foo, not just import foo.
# If you must do relative imports, use the explicit syntax from . import foo.
# Imports should be in sections in the following order: standard library modules, third party
# modules, your own modules. Each subsection should have imports in alphabetical order.



# Item 3: Know the Differences Between bytes, str, and unicode
# In python 3 there are two types that represent sequences of characters: bytes and str.
# In Python 3, bytes and str instances are never equivalent
# In Python 2, there are two types that represent sequences of characters: str and unicode.
# To convert Unicode characters to binary data， must use the encode method
# most common encoding is UTF-8. Importantly
# To convert binary data to Unicode characters, you must use the decode method.

# function to convert bytes to str
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value

# function to convert str to bytes
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value
print(to_bytes(123))

# write some random binary data to a file.
# in Python 3, operations involving file handles default to UTF-8 encoding
# That makes read and write operations on file handles expect str instances
# containing Unicode characters instead of bytes instances containing binary data.
# In Python 2, file operations default to binary encoding.
# so we have to use "wb“ instead of "w" in python 3. "w" can only write str but "wb" means
# data is being opened in write binary mode
with open("/tmp/random.bin", "wb") as f:
    f.write(os.urandom(10))
# This problem also exists for reading data from files. The solution is the same: Indicate
# binary mode by using 'rb' instead of 'r' when opening a file.

# remember !!! If you want to read or write binary data to/from a file, always open the file using a
# binary mode (like 'rb' or 'wb'). In Python 3, bytes contains sequences of 8-bit values, str contains sequences of
# Unicode characters. bytes and str instances can’t be used together with operators
# (like > or +).

