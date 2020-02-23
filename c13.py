# Learning python 5e page 205
# chapter 7 string fundementals


# String Conversion Tools
print(int("42"), str(42)) # Convert from/to string
print(repr(42))  # Convert to as-code string
# int and str are the generally prescribed to-number and to-string
# conversion techniques.
S = "42"
I = 1
print(int(S) + I)  # Force addition
print(S + str(I))  # Force concatenation


# Character code conversions
print(ord('s'))  # convert a single character to its underlying integer code (e.g., its ASCII byte value)
print(chr(115))
S = "5"
S = chr(ord(S) + 1)
print(S)
S = chr(ord(S) + 1)
print(S)
print(ord('5') - ord('0'))


# Convert binary digits to integer with ord
B = '1101'
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]
print(I)

int('1101', 2) # Convert binary to integer: built-in
bin(13) # Convert integer to binary: built-in


# Changing Strings I
S = 'spam'
S = S + 'SPAM!'
print(S)
S = S[:4] + 'Burger' + S[-1]
print(S)
S = 'splot'
S = S.replace('pl', 'pamal')  # replace
print(S)
# substitution metaphor
print('That is %d %s bird!' % (1, 'dead')) # Format expression
print('That is {0} {1} bird!'.format(1, 'dead'))  # Format method


# Method Call Syntax
# object.method(arguments)
S = 'spam'
result = S.find('pa')

# S.capitalize() S.ljust(width [, fill])
# S.casefold() S.lower()
# S.center(width [, fill]) S.lstrip([chars])
# S.count(sub [, start [, end]]) S.maketrans(x[, y[, z]])
# S.encode([encoding [,errors]]) S.partition(sep)
# S.endswith(suffix [, start [, end]]) S.replace(old, new [, count])
# S.expandtabs([tabsize]) S.rfind(sub [,start [,end]])
# S.find(sub [, start [, end]]) S.rindex(sub [, start [, end]])
# S.format(fmtstr, *args, **kwargs) S.rjust(width [, fill])
# S.index(sub [, start [, end]]) S.rpartition(sep)
# S.isalnum() S.rsplit([sep[, maxsplit]])
# S.isalpha() S.rstrip([chars])
# S.isdecimal() S.split([sep [,maxsplit]])
# S.isdigit() S.splitlines([keepends])
# S.isidentifier() S.startswith(prefix [, start [, end]])
# S.islower() S.strip([chars])
# S.isnumeric() S.swapcase()
# S.isprintable() S.title()
# S.isspace() S.translate(map)
# S.istitle() S.upper()
# S.isupper() S.zfill(width)
# S.join(iterable)

# Changing Strings II
S = 'spammy'
S = S[:3] + 'xx' + S[5:] # Slice sections from S
print(S)
S = 'spammy'
S = S.replace('mm', 'xx') # Replace all mm with xx in S
print(S)
print('aa$bb$cc$dd'.replace('$', 'SPAM'))
S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM') # Search for position
print(where) # Occurs at offset 4
S = S[:where] + 'EGGS' + S[(where+4):]
print(S)
S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.replace('SPAM', 'EGGS')) # Replace all
print(S.replace('SPAM', 'EGGS', 1)) # Replace one


S = 'spammy'
L = list(S)
L[3] = 'x'  # Works for lists, not strings
L[4] = 'x'
S = ''.join(L)  # join
print(S)
print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))

# Parsing Text
line = 'aaa bbb ccc'
col1 = line[0:3]
col3 = line[8:]
print(col1)
print(col3)
# split
line = 'aaa bbb ccc'
cols = line.split()
print(cols)
line = "i'mSPAMaSPAMlumberjack"
print(line.split("SPAM"))


# Other Common String Methods

line = "The knights who say Ni!\n"
print(line.rstrip())  #strip off whitespace at the end of a line of text,
print(line.upper()) # upper case
print(line.isalpha())  #test content
print(line.endswith('Ni!\n'))
print(line.startswith('The'))
print(line.find('Ni') != -1) #Search via method call or expression
sub = 'Ni!\n'
print(line.endswith(sub)) # End test via method call or slice
print(line[-len(sub):] == sub)


# String Formatting Expressions
# String formatting expressions: '...%s...' % (values)

# On the left of the % operator, provide a format string containing one or more embedded
# conversion targets, each of which starts with a %

# On the right of the % operator, provide the object (or objects, embedded in a tuple)
# that you want Python to insert into the format string on the left in place of the
# conversion target (or targets).

print('That is %d %s bird!' % (1, 'dead')) # the integer 1 replaces the %d in the format string on the left
# the string 'dead' replaces the %s.

print('%d %s %g you' % (1, 'spam', 4.0))
print('%s -- %s -- %s' % (42, 3.14159, [1, 2, 3]))

# Advanced Formatting Expression Syntax
# s String (or any object’s str(X) string)
# r Same as s, but uses repr, not str
# c Character (int or str)
# d Decimal (base-10 integer)
# i Integer
# u Same as d (obsolete: no longer unsigned)
# o Octal integer (base 8)
# x Hex integer (base 16)
# X Same as x, but with uppercase letters
# e Floating point with exponent, lowercase
# E Same as e, but uses uppercase letters
# f Floating-point decimal
# F Same as f, but uses uppercase letters
# g Floating-point e or f
# G Floating-point E or F
# % Literal % (coded as %%)

# %[(keyname)][flags][width][.precision]typecode
x = 1.23456789
print('%e | %f | %g' % (x, x, x))
print('%-6.2f | %07.2f | %+06.1f' % (x, x, x))# -6: reverse 6 chr.  07: 7 chr from left, space set as 0
print('integers: ...%d...%-6d...%06d' % (x, x, x))
print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0)) # * = 4 gives precision


# Dictionary-Based Formatting Expressions
print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})

reply = """
Greetings...
Hello %(name)s!
Your age is %(age)s
"""  # Template with substitution targets
values = {'name': 'Bob', 'age': 40}  # Build up values to substitute
print(reply % values)
food = 'spam'
qty = 10
print(vars())
print('%(qty)d more %(food)s' % vars())

# Formatting Method Basics
template = '{0}, {1} and {2}' # By position
print(template.format('spam', 'ham', 'eggs'))
template = '{motto}, {pork} and {food}' # By keyword
print(template.format(motto='spam', pork='ham', food='eggs'))
template = '{motto}, {0} and {food}' # By both
print(template.format('ham', motto='spam', food='eggs'))
template = '{}, {} and {}' # By relative position
print(template.format('spam', 'ham', 'eggs'))
template = '%s, %s and %s'  # Same via expression
print(template % ('spam', 'ham', 'eggs'))
template = '%(motto)s, %(pork)s and %(food)s'
print(template % dict(motto='spam', pork='ham', food='eggs'))
print('{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2]))
X = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
print(X)
Y = X.replace('and', 'but under no circumstances')
print(Y)

# Adding Keys, Attributes, and Offsets
import sys
print('My {1[kind]} runs {0.platform}'.format(sys, {'kind': 'laptop'})) # the attribute “platform” from the already imported sys module object
print('My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))
somelist = list('SPAM')
print('first={0[0]}, third={0[2]}'.format(somelist))
print('first={1}, last={0}'.format(somelist[0], somelist[-1]))  # [-1] fails in fmt
parts = somelist[0], somelist[-1], somelist[1:3] # [1:3] fails in fmt
print('first={0}, last={1}, middle={2}'.format(*parts)) # the use of *parts here to unpack a
# tuple’s items into individual function arguments



# Advanced Formatting Method Syntax "{1},{2},...".format("a","b","c",...)  or  "%.2f, %.e"%("a","b","c"....)
print('{0:10} = {2:10}'.format('spam', 123.4567,898)) # i:j, i th item in format of j char.
print('{0:>10} = {1:<10}'.format('spam', 123.4567)) # > 10 from right, <10 from left
print('{0.platform:>10} = {1[kind]:<10}'.format(sys, dict(kind='laptop')))
print('{:10} = {:10}'.format('spam', 123.4567))
print('{:>10} = {:<10}'.format('spam', 123.4567))
print('{.platform:>10} = {[kind]:<10}'.format(sys, dict(kind='laptop')))
print('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print('{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159))
print('{0:X}, {1:o}, {2:b}'.format(255, 255, 255)) # Hex, octal, binary
print(bin(255), int('11111111', 2), 0b11111111) # Other to/from binary
print(hex(255), int('FF', 16), 0xFF) #Other to/from hex
print('{0:.2f}'.format(1 / 3.0)) # Parameters hardcoded
print('%.2f'%(1 / 3.0)) # Ditto for expression
print('{0:.{1}f}'.format(1 / 3.0, 4)) # Take value from arguments
print('%.*f' % (4, 1 / 3.0)) # Ditto for expression .*f to ser precision
print('{0:.2f}'.format(1.2345)) # String method
print(format(1.2345, '.2f')) # Built-in function
print('%.2f' % 1.2345) #Expression
# {0:10} means the first positional argument in a field 10 characters wide
# {1:<10} means the second positional argument left-justified in a 10-character-wide field,
# {0.platform:>10} means the platform attribute of the first argument rightjustified in a 10-character-wide field
# {2:g} means the third argument formatted by default according to the “g” floating-point representation
# {1:.2f} designates the “f” floating-point format with just two decimal digits,