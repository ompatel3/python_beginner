# Learning python 5e page  581
# CHAPTER 20 Advanced Function Topics

# List Comprehensions Versus map
# chr it returns the character for an integer code point
print(ord('s'))
res = []
for x in 'spam':res.append(ord(x)) # Manual results collection
print(res)
[print(x) for x in range(5) if x % 2 == 0]
print(list(filter((lambda x: x % 2 == 0), range(5))))
print(list( map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(10))) ))

# formalcomprehension syntax
# [ expression for target1 in iterable1 if condition1
# for target2 in iterable2 if condition2 ...
# for targetN in iterableN if conditionN ]

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
print(res)
print([x + y for x in 'spam' for y in 'SPAM'])
print([x + y for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P', 'A')])
print([x + y + z for x in 'spam' if x in 'sm' for y in 'SPAM' if y in ('P', 'A')  for z in '123' if z > '1'])
print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])
# equivalent
res = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x, y))

# Example: List Comprehensions and Matrixes

M = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(M[1][2])

# col 2
col2 = [row[1] for row in M] # second num in each row
print(col2)
print([M[row][1] for row in (0, 1, 2)])
# Diagonals
diag = [M[x][x] for x in range(3)]
print(diag)
print([M[i][len(M)-1-i] for i in range(len(M))])

# add 10 to each ele in matrix
L = [[1, 2, 3], [4, 5, 6],[7,8,9]]
for i in range(len(L)):
    for j in range(len(L[i])): # Update in place
        L[i][j] += 10
print(L)
# or
print([col + 10 for row in M for col in row])
print([[col + 10 for col in row] for row in M])

res = []
for row in M: # Statement equivalents
    for col in row: # Indent parts further right
        res.append(col + 10)
print(res)

res = []
for row in M:
    tmp = [] # Left-nesting starts new list
    for col in row:
        tmp.append(col + 10)
        res.append(tmp)
print(res)
# ele in M1 * ele in M2 with the same pos
N = [[1, 2, 3], [4, 5, 6],[7,8,100]]
print([M[row][col] * N[row][col] for row in range(3) for col in range(3)])
print([[M[row][col] * N[row][col] for col in range(3)] for row in range(3)])
print([[M[row][col] * N[row][col] for row in range(3)] for col in range(3)])


# zip function  zip(A,B)： each (ele_A, ele_B)
print([[col1 * col2 for (col1, col2) in zip(row1, row2)] for (row1, row2) in zip(M, N)])

# (row 1, row 2) = (Mi , Ni)
# (col1, col2) = (Mi[j], Ni[j])
res = []
for (row1, row2) in zip(M, N):
    tmp = []
    for (col1, col2) in zip(row1, row2):
        tmp.append(col1 * col2)
    res.append(tmp)

# matrix multiply

def mul(M, N):
    fin = []
    res = []
    col = 0
    while col < len(M):
        for i in range(len(N[0])):
            temp = 0
            for row in range(len(M[0])):
                temp += M[col][row] * N[row][i]
            res.append(temp)
        col += 1
    for j in range(len(M)):
        fin.append(res[(j*len(N[0])):(j+1)*len(N[0])])
    return fin

M1 = [[1,2,3,4,5,6],[2,3,4,5,6,88],[6,6,4,3,2,45]] # 3*6 matrix
M2 = [[1,2,3],[7,8,9],[1,1,1],[2,2,2],[3,3,3],[6,6,6]] # 6*3 matrix
print(mul(M1, M2))

# Generator Functions and Expressions
# yield
def gensquares(N):
    for i in range(N):
        yield i ** 2
print(gensquares(5))  # it is not a value but a generator!!!
for i in gensquares(5): # Resume the function
    print(i, end=' : ') # Print last yielded value

x = gensquares(4)
print(next(x))
print(x.__next__())
print(x.__next__())

# Why generator functions
def buildsquares(n):
    res = []
    for i in range(n): res.append(i ** 2)
    return res

for x in buildsquares(5): print(x, end=' : ')
for x in [n ** 2 for n in range(5)]: print(x, end=' : ')
for x in map((lambda n: n ** 2), range(5)):print(x, end=' : ')

# lowercase to uppercase for each ele
def ups(line):
    for sub in line.split(','): # Substring generator
         yield sub.upper()
for i in ups('aaa,bbb,ccc'): print(i)
tuple(ups('aaa,bbb,ccc')) # All iteration contexts
print({ i: s for (i, s) in enumerate(ups('aaa,bbb,ccc'))}) # enumerate(A)---(i, A[i])


# Extended generator function protocol: send versus next
def gen():
    for i in range(10):
        X = yield i
        print(X)
G = gen()
print(next(G))
print(G.send(77))  # send value to yield expression
print(G.send(88))
print(G.send(2))
print(G.__next__())

# Generator Expressions: Iterables Meet Comprehensions
print([x ** 2 for x in range(4)])  # list
print((x ** 2 for x in range(4)))  # generator
print(list(x ** 2 for x in range(4)))  # List comprehension equivalence
G = (x ** 2 for x in range(4))
print(iter(G) is G)
print(next(G))
print(G.__next__())
print(G.__next__())

for num in (x ** 2 for x in range(4)):print('%s, %s' % (num, num / 2.0)) # Calls next() automatically
''.join(x.upper() for x in 'aaa,bbb,ccc'.split(','))  # 'aaa,bbb,ccc'.split(',') is generator
a, b, c = (x + '\n' for x in 'aaa,bbb,ccc'.split(','))  # assign generator
print(a,b,c)

sum(x ** 2 for x in range(4)) # take sum
sorted(x ** 2 for x in range(4)) # Parens optional
sorted((x ** 2 for x in range(4)), reverse=True) # Parens required

# Generator expressions versus map
list(map(abs, (-1, -2, 3, 4))) # map
list(abs(x) for x in (-1, -2, 3, 4)) # generator
list(map(lambda x: x * 2, (1, 2, 3, 4)))  # map
list(x * 2 for x in (1, 2, 3, 4)) # Simpler as generator?

line = 'aaa,bbb,ccc'
print('...'.join([x.upper() for x in line.split(',')])) # Makes a .... list
print('...'.join(x.upper() for x in line.split(',')))
''.join(map(str.upper, line.split(','))) # map results
''.join(x * 2 for x in line.split(','))
''.join(map(lambda x: x * 2, line.split(',')))

# map's ouput is turple/generator
# list(generator/ turple)-----make it turple

[x * 2 for x in [abs(x) for x in (-1, -2, 3, 4)]]  # Nested generator
list(map(lambda x: x * 2, map(abs, (-1, -2, 3, 4)))) # Nested maps
list(x * 2 for x in (abs(x) for x in (-1, -2, 3, 4))) # Nested generators

import math
list(map(math.sqrt, (x ** 2 for x in range(4)))) # Nested combinations
list(map(abs, map(abs, map(abs, (-1, 0, 1)))))
list(abs(x) for x in (abs(x) for x in (abs(x) for x in (-1, 0, 1))))
print(list(abs(x) * 2 for x in (-1, -2, 3, 4)))
print((list(map(lambda x: abs(x)*2, (-1, -2, 3, 4)))))

"...".join(x for x in line.split() if len(x) > 1) # Generator with 'if'
'...'.join(filter(lambda x: len(x) > 1, line.split())) # Similar to filter
''.join(x.upper() for x in line.split() if len(x) > 1)
''.join(map(str.upper, filter(lambda x: len(x) > 1, line.split())))
''.join(x.upper() for x in line.split() if len(x) > 1)


#Generator Functions Versus Generator Expressions
G = (c * 4 for c in 'SPAM')
print(list(G))

def timesfour(S):  # generator func
    for c in S:
        yield c * 4
G = timesfour('spam')
print(list(G))
G = (c * 4 for c in 'SPAM')
print(G)
print(next(G))


line = 'aa bbb c'
''.join(x.upper() for x in line.split() if len(x) > 1) # Expression
def gensub(line): # Function
    for x in line.split():
        if len(x) > 1:
            yield x.upper()
print(''.join(gensub(line)))

# Generators Are Single-Iteration Objects
I3 = iter(c * 4 for c in 'SPAM')
next(I3)
L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)
next(I1)
next(I2)


def both(N):
    for i in range(N): yield i
    for i in (x ** 2 for x in range(N)): yield i
print(list(both(5)))
print(' : '.join(str(i) for i in both(5)))