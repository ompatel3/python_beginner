# Learning python 5e page 133-174
# chapter 5 numeric type
# A complete inventory of Python’s numeric toolbox includes:
# Integer and floating-point objects
# Complex number objects
# Decimal: fixed-precision objects
# Fraction: rational number objects
# Sets: collections with numeric operations
# Booleans: true and false
# Built - in functions and modules: round, math, random, etc.
# Expressions; unlimited integer precision; bitwise operations; hex, octal, and binary formats


# Numeric Literals
# 1234, −24, 0, 99999999999999 Integers (unlimited size)
# 1.23, 1., 3.14e-10, 4E210, 4.0e+210 Floating-point numbers
# 0o177, 0x9ff, 0b101010 Octal, hex, and binary literals
# 3+4j, 3.0+4.0j, 3J Complex number literals
# set('spam'), {1, 2, 3, 4}, set
# Decimal('1.0'), Fraction(1, 3) Decimal and fraction extension types
# bool(X), True, False Boolean type and constants


# Built-in Numeric Tools
# Expression operators: +, -, *, /, >>, **, &, etc.
# Built-in mathematical functions: pow, abs, round, int, hex, bin, etc.
# Utility modules: random, math, etc.

# Python Expression Operators
# yield like return in an order
def simpleGeneratorFun(): #  A generator function that yields 1 for the first time, 2 second time and 3 third time
    yield 1
    yield "ac"
    yield 3
for value in simpleGeneratorFun():  # Driver code to check above generator function
    print(value)
def simpleGeneratorFun(): #  A generator function that only return the first one
    return 1
    return "ac"
    return 3
print(simpleGeneratorFun())

# lambda args: expression
f = lambda x: x * x  #  define a lambda function with one argument.
print(f(5))

f = lambda x, y: x * y  #   define a lambda that takes two integer arguments and returns their product.
print(f(5, 2))

f = lambda: True  #  define a lambda function that takes no arguments and returns True.
print(f())

L = [1, 2, 3, 4]
print(list(map(lambda x: x**2, L)))  # map(fun, seq) calls the input function on each item of the sequence.
print(list(filter(lambda x: x % 2 == 0, [1, 3, 2, 5, 20, 21])))  # filtter(fun, seq) fillter the input function on each item of the sequence.
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
Alex = Employee('Alex', 20)
Amanda = Employee('Amanda', 30)
David = Employee('David', 15)
L = [Alex, Amanda, David]
L.sort(key=lambda x: x.age)  # L sorted by age of x for each x in L
print([item.name for item in L])  # return the name based on their age

# x if y else z
# x or y
# x and y
# not x
# x in y, x not in y
# x is y, x is not y
# x < y, x <= y, x > y, x >= y
# x == y, x != y
# x | y  Bitwise OR, set union
# x ^ y Bitwise XOR, set symmetric difference
# x & y Bitwise AND, set intersection
# x << y, x >> y Shift x left or right by y bits
# x + y x – y Addition, concatenation, Subtraction, set difference
# x * y Multiplication, repetition;
# x % y Remainder, format;
# x / y, x // y Division: true and floor
# −x, +x Negation, identity
# ˜x Bitwise NOT (inversion)
# x ** y Power (exponentiation)
# x[i] Indexing (sequence, mapping, others)
# x[i:j:k] Slicing
# x(...) Call (function, method, class, other callable)
# x.attr Attribute reference
# (...) Tuple, expression, generator expression
# [...] List, list comprehension
# {...} Dictionary, set, set and dictionary comprehensions

int(3.1415) # Truncates float to integer
float(3) # Converts integer to float
a = 3
b = 4
print(a + 1, a - 1) # Addition (3 + 1), subtraction (3 − 1)
print(b * 3, b / 2) # Multiplication (4 * 3), division (4 / 2)
print(a % 2, b ** 2) # Modulus (remainder), power (4 ** 2)
print(2 + 4.0, 2.0 ** b)  # Mixed-type conversions
print(b / (2.0 + a))
num = 1 / 3.0
print('%e' % num)  # String formatting expression
print('%4.2f' % num)  # Alternative floating-point format

# Comparisons: Normal and Chained
X = 2
Y = 4
Z = 6
print(X < Y and Y < Z)
print(X < Y < Z)
print(1 > 2 > 3.0 > 4)

# Division: Classic, Floor, and Truev
print(10 / 4)  # keeps remainder
print(10 / 4.0)  # keeps remainder
print(10 // 4)  # truncates remainder
print(10 // 4.0)

import math
print(math.floor(2.5))  # Closest number below value
print(math.floor(-2.5))
print(math.trunc(2.5))  # Truncate fractional part (toward zero)
print(math.trunc(-2.5))
print((5 / 2), (5 / 2.0), (5 / -2.0), (5 / -2))  # true division
print((5 // 2), (5 // 2.0), (5 // -2.0), (5 // -2))  # floor division
print((9 / 3), (9.0 / 3), (9 // 3), (9 // 3.0))  # Both


# Complex Numbers
print(1j * 1J)
print(2 + 1j * 3)
print((2 + 1j) * 3)

#Hex(0x), Octal(0o), Binary(0b): Literals and Conversions
print(0o1, 0o20, 0o377)  # Octal literals: base 8, digits 0-7
print(0x01, 0x10, 0xFF)  # Hex literals: base 16, digits 0-9/A-F
print(0b1, 0b10000, 0b11111111)  # Binary literals: base 2, digits 0-1
print(oct(64), hex(64), bin(64))  # Numbers=>digit strings
print(64, 0o100, 0x40, 0b1000000) # Digits=>numbers in scripts and strings
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))  # int --- digit number
print(int('0x40', 16), int('0b1000000', 2))  # Literal forms supported too


#Bitwise Operations
x = 1  # 1 decimal is 0001 in bits
print(bin(x))
print(x << 2)  # Shift left 2 bits: 0100 = 4
print(x | 2)  # Bitwise OR (either bit=1): 0011, combine bits (0001|0010 = 0011))
print(x & 1)  # Bitwise AND (both bits=1): 0001, (0001&0001 = 0001) both
X = 0b0001 # Binary literals
print(X << 2)  # Shift left
print(bin(X << 2)) # Binary digits string
print(bin(X | 0b010)) # Bitwise OR: either 0b011
print(bin(X & 0b1))  # Bitwise AND: both
X = 0xFF # Hex literals
print(bin(X))
print(bin(X ^ 0b10101010))  # Bitwise XOR: either but not both
print(int('01010101', 2))  # Digits=>number: string to int per base
hex(85) # Number=>digits: Hex digit string
print(bin(X), X.bit_length(), len(bin(X)) - 2)


# Other Built-in Numeric Tools
import math
import random
print(math.pi, math.e)  # Common constants
print(math.sin(2 * math.pi / 180)) # Sine, tangent, cosine
print(math.sqrt(144), math.sqrt(2)) # Square root
print(pow(2, 4), 2 ** 4, 2.0 ** 4.0) # Exponentiation (power)
print(abs(-42.0), sum((1, 2, 3, 4))) # Absolute value, summation
print(min(3, 1, 2, 4), max(3, 1, 2, 4))  # Minimum, maximum)
print(math.floor(2.567), math.floor(-2.567))  # Floor (next-lower integer)
print(math.trunc(2.567), math.trunc(-2.567)) # Truncate (drop decimal digits)
print(int(2.567), int(-2.567)) # Truncate (integer conversion)
print(round(2.567), round(2.467), round(2.567, 2)) # Round
print('%.1f' % 2.567, '{0:.2f}'.format(2.567)) # Round for display
print((1 / 3.0), round(1 / 3.0, 2), ('%.2f' % (1 / 3.0)))
print(1234567890 ** .5, pow(1234567890, .5))
print(random.randint(1, 10)) # integer from 1 to 10
print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))
suits = ['hearts', 'clubs', 'diamonds', 'spades']
random.shuffle(suits)  # shuffle
print(suits)


# decimal
from decimal import Decimal
print(0.1 + 0.1 + 0.1 - 0.3)  # The result is close to zero
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print(Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30'))
print(Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3))

# Setting decimal precision globally
import decimal
print(decimal.Decimal(1) / decimal.Decimal(7))
decimal.getcontext().prec = 4 # Fixed precision
print(decimal.Decimal(1) / decimal.Decimal(7))
decimal.getcontext().prec = 2
pay = decimal.Decimal(str(1999 + 1.33))
print(pay)
with decimal.localcontext() as ctx:
    ctx.prec = 2
print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))


# Fraction basics
from fractions import Fraction
x = Fraction(1, 3)  # Numerator, denominator
y = Fraction(4, 6)  # Simplified to 2, 3 by gcd
print(y)
print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction('.25') + Fraction('1.25'))
print(Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10))

# Fraction conversions
print((2.5).as_integer_ratio())  # float object method
f = 2.293845
z = Fraction(*f.as_integer_ratio()) # Convert float -> fraction: two args
print(z)
x = Fraction(1, 3)
print(float(x))  # Convert fraction -> float
print(Fraction.from_float(2.5)) # Convert float -> fraction: other way
print(Fraction(*(1.75).as_integer_ratio()))

a = x + Fraction(*(4.0 / 3).as_integer_ratio())  # 5 / 3 (or close to it!)
print(a)
print(a.limit_denominator(10))  # Simplify to closest fraction, denominator<=10


# set
x = set('abcde')
y = set(["a","b","f","g"])
z = {"a","b","a","f"}
print(z)
print(x)
print("e" in x)
print("e" in y)
print(x - y)  # Difference in x not in y
print(x | y)  # Union
print(x & y)  # Intersection
print(x ^ y)  # Symmetric difference (XOR) union of x and y - intersection of x and y
print(x > y, x < y) # Superset, subset
# set method
z = x.intersection(y)  #Intersection
print(z)
z.add('SPAM')  # Insert one item
print(z)
z.update(set(['X', 'Y'])) # Merge: in-place union
print(z)
z.remove('b') # Delete one item
print(z)
# list comprehensions for set
for item in set('abc'): print(item * 3)
S = set([1, 2, 3])
S | set([3, 4])  # Expressions require both to be sets
print(S.union([3, 4]))
print(S.intersection((1, 3, 5)))
print(S.issubset(range(-5, 5)))  # is subset?
print({x for x in 'spam'})
# use sets
L = [1, 2, 1, 3, 2, 4, 5]
L = list(set(L)) # Remove duplicates
print(L)
list(set(['yy', 'cc', 'aa', 'xx', 'dd', 'aa'])) # But order may change
print(set([1, 3, 5, 7]) - set([1, 2, 4, 5, 6])) # Find list differences
print(set('abcdefg') - set('abdghij')) # Find string differences
print(set('spam') - set(['h', 'a', 'm']))  # Find differences, mixed
print(set(dir(bytes)) - set(dir(bytearray)))  # In bytes but not bytearray
L1, L2 = [1, 3, 5, 2, 4], [2, 5, 3, 4, 1]
print(L1 == L2) # Order matters in sequences
print(set(L1) == set(L2))  # Order-neutral equality
print(sorted(L1) == sorted(L2)) # Similar but results ordered


# Booleans
type(True)
print(isinstance(True, int))
print(True == 1)  # Same value
print(True is 1)  # But a different object
print(True or False) # Same as: 1 or 0
print(True + 4)