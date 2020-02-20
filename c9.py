# Learning python E5
# Part 2 Types and operations

# object type
# Built-in objects preview
# Numbers: 1234, 3.1415, 3+4j, 0b111, Decimal(), Fraction()
# Strings: 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
# Lists: [1, [2, 'three'], 4.5], list(range(10))
# Dictionaries: {'food': 'spam', 'taste': 'yum'}, dict(hours=10)
# Tuples: (1, 'spam', 4, 'U'), tuple('spam'), namedtuple
# Files: open('eggs.txt'), open(r'C:\ham.bin', 'wb')
# Sets: set('abc'), {'a', 'b', 'c'}
# Other core types: Booleans, types, None
# Program unit types: Functions, modules, classes (Part IV, Part V, Part VI)
# Implementation-related types: Compiled code, stack tracebacks (Part IV, Part VII)

# numbers
import math
import random
print(123 + 222)  # Integer addition
print(1.5 * 4)  # Floating-point multiplication
print(2 ** 100)  # 2 to the power 100, again
print(len(str(2 ** 1000000)))   # How many digits in a really BIG number?
print(math.pi)  # pi
print(math.sqrt(85))  # 85^2
print(random.random())  # Return the random floating point number in the range [0.0, 1.0).
print(random.choice([1, 2, 3, 4]))  # Return a random element from the non-empty sequence seq.
# If seq is empty, raises IndexError.



# Strings
S = 'Spam'  # Make a 4-character string, and assign it to a name
print(len(S))  # Length
print(S[0])  # The first item in S, indexing by zero-based position
print(S[1])  # The second item from the left
print(S[-1])  # The last item from the end in S
print(S[len(S)-1])  # Negative indexing, the hard way
print(S)  # A 4-character string
print(S[1:3])  # Slice of S from offsets 1 through 2 (not 3)
print(S[1:])  # Everything past the first (1:len(S))
print(S[:3])  # Same as S[0:3]
print(S[:-1])  # Everything but the last again, but simpler (0:-1)
print(S[:])  # All of S as a top-level copy (0:len(S))
print(S + 'xyz')  # Concatenation
print(S * 8)  # Repetition

# Immutability
# strings are immutable in Python!!!! so we cannot change the string through string operations
# but we can always build a new one and assign it to the same name
# generally speaking, Numbers, strings, and tuples are immutable in python!
# lists, dictionaries, and sets are not
try:
    S[0] = 'z'
except TypeError as err:
    print("TypeError:" + str(err))

S = 'z' + S[1:] # But we can run expressions to make new objects
print(S)

S = 'shrubbery'
L = list(S)  # Expand to a list: [...]
print(L)
L[1] = "c"  # Change it in place
''.join(L)  # Join with empty delimiter
B = bytearray(b'spam')  # using bytearray to translate spam into a bytes/list hybrid (ahead)
B.extend(b'eggs')  # add eggs to the string, 'b' needed in python 3,
print(B)  # untranslated string
print(B.decode())  # Translate to normal string
# The bytearray supports in-place changes for text, but only for text whose characters
# are all at most 8-bits wide (e.g., ASCII).

# Type-Specific Methods
S = 'Spam'
print(S.find('pa'))  # Find the offset of a substring in S
#  return −1 if it is not present
print(S.replace('pa', 'XYZ'))  # Replace occurrences of a string in S with another
line = 'aaa,bbb, ccccc, dd'
print(line.split(','))  # Split on a delimiter into a list of substrings
S = 'spam'
print(S.upper())  # Upper- and lowercase conversions
S.isalpha()  # Content tests: isalpha, isdigit, etc
line = 'aaa, bbb, ccccc, d\nd\n' # \n means a white space
print(line)
print(line.rstrip())  # Remove whitespace characters on the right side
print(line.rstrip().split(','))  # Combine two operations
print('%s, eggs, and %s' % ('spam', 'SPAM!'))  # formatting expression
print('{}, eggs, and {}'.format('spam', 'SPAM!'))  # Numbers optional
print('{:,.2f}'.format(296999.2567))
print('%.2f | %+05d' % (3.14159, -42))

# getting help
print(dir(S))  # dir function simply gives the methods’ names
print(S.__add__('NI!'))  # using double underscores method of strings
help(S.replace)  # use help to find more details

# Other Ways to Code Strings
S = 'A\nB\tC'  # \n is end-of-line, \t is tab
print(S)
print(len(S))  # Each stands for just one character
print(ord('\n'))  # \n is a byte with the binary value 10 in ASCII
S = 'A\0B\0C'  # \0, a binary zero byte, does not terminate string
print(S)

# Unicode Strings
# handling characters in the Japanese and Russian alphabets that are outside the
# ASCII set requires Unicode support

print('sp\xc4m')  # normal str strings are Unicode text
print(b'a\x01c')  # bytes strings (b') are byte-based data
print("sp\u00c4m")  # Unicode strings are a distinct type
print('a\x01c')  # Normal str strings contain byte-based text/data
print('spam'.encode('utf8'))  # Encoded to 4 bytes in UTF-8 in files
print('spam'.encode('utf16'))  # But encoded to 10 bytes in UTF-16
print('sp\xc4\u00c4\U000000c4m')
print('\u00A3', '\u00A3'.encode('latin1'), b'\xA3'.decode('latin1'))