# Learning python 5e page  604
# CHAPTER 20 Advanced Function Topics


# Generation in Built-in Types, Tools, and Classes

D = {'a':1, 'b':2, 'c':3}
x = iter(D) # dic generator
print(next(x))
print(next(x))

for key in D:
    print(key, D[key])


for line in open('test.txt'): # file generator
    print(line, end='')


# Generators and library tools: Directory walkers
import os
for (root, subs, files) in os.walk('.'): # Directory walk generator
    for name in files: # A Python 'find' operation
        if name.startswith('call'):
            print(root, name)

# Generators and function application
def f(a, b, c): print('%s, %s, and %s' % (a, b, c))
f(0, 1, 2)
f(*range(3))
f(*(i for i in range(3)))


D = dict(a='Bob', b='dev', c=40.5)
f(a='Bob', b='dev', c=40.5)
f(**D)
f(*D)
f(*D.values())

for x in 'spam': print(x.upper(), end=' ')
list(print(x.upper(), end=' ') for x in 'spam')
print(*(x.upper() for x in 'spam'))


# Example: Generating Scrambled Sequences
L, S = [1, 2, 3], 'spam'
for i in range(len(S)): # For repeat counts 0..3
    S = S[1:] + S[:1] # Move front item to the end
    print(S, end=' ')
for i in range(len(L)):
    L = L[1:] + L[:1] # Slice so any sequence type works
    print(L, end=' ')


# Simple functions
def scramble(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res
print(scramble('spam'))


def scramble(seq):
    return [seq[i:] + seq[:i] for i in range(len(seq))]
print(scramble('spam'))

for x in scramble((1, 2, 3)):print(x, end=' ')

# Generator functions
def scramble(seq):
    for i in range(len(seq)):
        seq = seq[1:] + seq[:1]  # Generator function
        yield seq

def scramble(seq):
    for i in range(len(seq)): # Generator function
        yield seq[i:] + seq[:i]

for x in scramble((1, 2, 3)): # for loops generate results
    print(x, end=' ')
S = "spam"
G = (S[i:] + S[:i] for i in range(len(S)))
print(list(G))
F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))
print(F(S))
# use list to show generator
print(list(F(S)))
print(list(F([1, 2, 3])))

for x in F((1, 2, 3)):
    print(x, end=' ')

# Permutations: All possible combinations
def permute1(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i + 1:]  # Delete current node
            for x in permute1(rest):  # Permute the others
                res.append(seq[i:i+1] + x)  # Add node at front
        return res
print(permute1('abc'))
print(permute1('c'))
# if seq = c, i=0, rest =[], res = c
# if seq = bc, i=0, rest = c, x=c, res = bc, i=1, rest = b, x=b, res = cb
# if seq = abc, i=0, rest = bc, p(bc)= (bc, cb), x = bc, res = abc, x=cb, res = acb
#               i=1, rest = ac, p(ac)= (ac, ca), x = ac. res = bac. x=ca, res = bca
#               i=1, rest = ab, p(ab)= (ab, ba), x = ab. res = cab. x=ba, res = cba

# how to find a permutation:
# 1. given a string, take the first item out, p(rest), add first item in front of p(rest)
# 2. if it has only one item, take it out it will be empty set, p(empty set)= empty set, add it to the front of empty set

# generator function
def permute2(seq):
    if not seq: # Shuffle any sequence: generator
        yield seq # Empty sequence
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:] # Delete current node
            for x in permute2(rest): # Permute the others
                yield seq[i:i+1] + x # Add node at front
print(list(permute2('abcdefg')))
G = permute2('abc')
print(next(G))


# import math
# print(math.factorial(10))
# seq = list(range(10))
# p1 = permute1(seq)
# print(len(p1), p1[0], p1[1])
# import random
# seq = list(range(20))
# random.shuffle(seq)
# print(seq)
# p = permute2(seq)
# print(next(p))

# Example: Emulating zip and map with Iteration Tools
S1 = 'abc'
S2 = 'xyz123'
print(list(zip(S1, S2)))
print(list(zip([-2, -1, 0, 1, 2])))
print(list(zip([1, 2, 3], [2, 3, 4, 5])))


# Coding your own map(func, ...)
def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res
print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))

# Using a list comprehension
def mymap(func, *seqs):return [func(*args) for args in zip(*seqs)]
print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))


def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        yield func(*args)

def mymap(func, *seqs): return (func(*args) for args in zip(*seqs))
print(list(mymap(abs, [-2, -1, 0, 1, 2])))
print(list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])))
