# Learning python 5e page 239
# chapter 8 Lists and Dictionaries

L = [] # An empty list
L = [123, 'abc', 1.23, {}] #Four items: indexes 0..3
L = ['Bob', 40.0, ['dev', 'mgr']]  #Nested sublists
L = list('spam') #List of an iterable’s items, list of successive integers
L = list(range(-4, 4))
print(L)
# L[i] L[i][j] L[i:j] len(L)  Index, index of index, slice, length
# L1 + L2, L * 3 Concatenate, repeat
for x in L: print(x) #Iteration
3 in L #membership
print(L)
L.append(4)  # Methods: growing
print(L)
L.extend([5,6,7])
L.insert(2, "X")
print(L)
L.index("X")  #Methods:searching
L.count("X")
# L.sort()  # sorting, reversing
L.reverse()
L.copy()
# L.clear()
print(L)
L.pop(0) #statements: shrinking
L.remove("X")
del L[0]  # del L[i:j]
print(L)
# L[i:j] = [] L[i] = 3 L[i:j] = [4,5,6] Index assignment, slice assignment
L = [x**2 for x in range(5)] # List comprehensions and maps
list(map(ord, 'spam'))


# basic operations
print([1, 2] + list("34"))
for x in [1, 2, 3]: print(x, end=' ')
res = [c * 4 for c in 'SPAM']  # List comprehensions

# map(fun, object)
list(map(abs, [-1, -2, 0, 1, 2]))

# matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[2][0])

# index assignment
L = ['spam', 'Spam', 'SPAM!']
L[1] = 'eggs'
print(L)

L = [1, 2, 3]
L[1:2] = [4, 5] # Replacement/insertion
L[1:1] = [6, 7] # Insertion (replace nothing)
L[1:2] = [] # Deletion (insert nothing)
L[:0] = [2, 3, 4]  # insert at front
L[len(L):] = [5, 6, 7] # insert at end
L.extend([8, 9, 10]) # Insert all at end, named method
L = ['eat', 'more', 'SPAM!']
L.sort() # Sort list items ('S' < 'e')
print(L)
L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower) # Normalize to lowercase
print(L)
L = ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True) # Change sort order
sorted(L, key=str.lower, reverse=True) # same but built in
print(L)
print(sorted([x.lower() for x in L], reverse=True))



# Dictionaries
D = dict(name='Bob', age=40)
D = dict([('name', 'Bob'), ('age', 40)])
print(D)
D['name']= "bob"
D.keys() # all keys
D.values() # all values
print(D.items())
D.copy() # copy (top-level),
#D.clear() clear (remove all items),
# D.update(D2) merge by keys



D = {'spam': 2, 'ham': 1, 'eggs': 3}
print(list(D.keys()))
D['ham'] = ['grill', 'bake', 'fry']  # Change entry (value=list)
print(D)
del D['eggs'] # Delete entry
D['brunch'] = 'Bacon' # Add new entry
print(list(D.values()))
print(list(D.items()))
print(D)

print(D.get('ham'))  # A key that is there
print(D.get('toast')) # A key that is missing
D2 = {'toast':4, 'muffin':5}
D.update(D2)  # add new entries
print(D)
D.pop('muffin')
D.pop('toast')  #Delete and return from a key
print(D)



# Movie Database
table = {'1975': 'Holy Grail','1979': 'Life of Brian','1983': 'The Meaning of Life'}
year = '1983'
movie = table[year] # dictionary[Key] => Value
print(movie)

for year in table: print(year + '\t' + table[year])  # Same as: for year in table.keys()

table = {'Holy Grail': '1975','Life of Brian': '1979', 'The Meaning of Life': '1983'}
print(table['Holy Grail'])
print(list(table.items()))
print([title for (title, year) in table.items() if year == '1975'])
V = '1975'
print([key for (key, value) in table.items() if value == V])
print([key for key in table.keys() if table[key] == V])


#When you use lists, it is illegal to assign to an offset that is off the end of the list:
# L = []  L[99] = 'spam'  wrong!
D = {}
D[99] = 'spam'
print(D)


#Using dictionaries for sparse data structures: Tuple keys
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99
X = 2; Y = 3; Z = 4
print(Matrix[(X, Y, Z)])
print(Matrix)
if (2, 3, 6) in Matrix: # Check for key before fetch
    print(Matrix[(2, 3, 6)])
else:print(0)

try:
    print(Matrix[(2, 3, 6)]) # Try to index
except KeyError: # Catch and recover
    print(0)
print(Matrix.get((2, 3, 4),0))
print(Matrix.get((2, 3, 999),100)) # Doesn't exist: use default arg




# Nesting in dictionaries
rec = {}
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['job'] = 'developer/manager'
print(rec['name'])
rec = {'name': 'Bob','jobs': ['developer', 'manager'],'web': 'www.bobs.org/˜Bob','home': {'state': 'Overworked', 'zip': 12345}}
print(rec['jobs'][1])
rec['home']['zip']

db = []
db.append(rec)
print(db)
print(db[0]['jobs'])  # it is a list with only one element!

db = {}
db['bob'] = rec
print(db)
db['bob']['jobs']   # it is a dic with only one element!


#Other Ways to Make Dictionaries
{'name': 'Bob', 'age': 40} #Traditional literal expression
D = {}  # Assign by keys dynamically
D['name'] = 'Bob'
D['age'] = 40
dict(name='Bob', age=40) # dict keyword argument form
dict([('name', 'Bob'), ('age', 40)]) # dict key/value tuples form
print(dict.fromkeys(['a', 'b'], ["123","456"]))

#zip(keyslist, valueslist)===> key 1 => value 1
print(dict(zip(['a', 'b', 'c'], ['1', '2', '3'])))  #dict(zip(keyslist, valueslist)) # Zipped key/value tuples form (ahead
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))


D = dict(name='Bob', age=40.5, jobs=['dev', 'mgr'])
D['jobs'].remove('mgr')
# set
D= set()
D.add('state1')
print(D)

D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print(D)
D = {x: x ** 2 for x in [1, 2, 3, 4]}
print(D)
D = {c: c * 4 for c in 'SPAM'}
print(D)
D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print(D)
D = dict.fromkeys(['a', 'b', 'c'], 0)
print(D)
D = {k:0 for k in ['a', 'b', 'c']} # Same, but with a comprehension
print(D)
D = dict.fromkeys('spam')  # D = {k: None for k in 'spam'}
print(D)

D = dict(a=1, b=2, c=3)
print(D)
K = D.keys()
print(K)
print(list(K))
V = D.values()
print(list(V))

for k in D.keys(): print(k)
for key in D: print(key)


# Dictionary views and sets
print(K | {'x': 4})
D = {'a': 1, 'b': 2, 'c': 3}
print(D.keys() & {'b': 1}) # Intersect keys and dict
print(D.keys() | {'b', 'c', 'd'}) # Union keys and set
D = {'a': 1}
print(D.items() | D.keys()) # Union view and view
print(D.items() | D) # dict treated same as its keys
print(dict(D.items() | {('c', 3), ('d', 4)})) # dict accepts iterable sets too
D = {'a': 1, 'b': 2, 'c': 3}
Ks = D.keys()
Ks = list(Ks)
print(Ks.sort())  # sort after converting to list
Ks = D.keys()
for k in sorted(Ks): print(k, D[k])