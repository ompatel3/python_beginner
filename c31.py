# Learning python 5e page  887
# CHAPTER 30
# Operator Overloading

# __sub__ method
from number import Number
X = Number(5)  # Number.__init__(X, 5)
Y = X - 2  # Number.__sub__(X, 2)
print(Y.data)

# Common Operator Overloading Methods


# Indexing and Slicing: __getitem__ and __setitem__
class Indexer:
    def __getitem__(self, index):
        return index ** 2
X = Indexer()
print(X[2])
for i in range(5): print(X[i], end=' ')  # Runs __getitem__(X, i) each time

class Indexer:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index): # Called for index or slice
        print('getitem:', index)
        return self.data[index] # Perform index or slice
X = Indexer()
print(X[0])
print(X[1])
print(X[2])
print(X[3])
print(X[2:4])
print(X[::2])

class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int): # Test usage mode
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)
X = Indexer()
print(X[99])
print(X[1:99:2])
print(X[1:])

class C:
    def __index__(self):
         return 255
X = C()
hex(X)  # Integer value
bin(X)
oct(X)


class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]

X = StepperIndex()
X.data = "Spam"
X[1]
for item in X: # for loops call __getitem__
    print(item, end=' ')

# Iterable Objects: __iter__ and __next__
class Squares:
    def __init__(self, start, stop): # Save state when created
        self.value = start
        self.stop = stop
    def __iter__(self): # Get iterator object on iter
        return self
    def __next__(self): # Return a square on each iteration
        if self.value == self.stop: # Also called by next built-in
            raise StopIteration
        self.value += 1
        return self.value ** 2
for i in Squares(1, 22): # for calls iter, which calls __iter__
    print(i, end = ' ')
for i in Squares(1, 10): print(i, end=' ')
X = Squares(1, 5)
I = iter(X)
print(next(I))
print(next(I))
print(next(I))
print(next(I))

print([n for n in Squares(1, 5)])
X = list(Squares(1, 5))
print(tuple(X), tuple(X))

def gsquares(start, stop):
    for i in range(start, stop + 1):
        yield i ** 2
for i in gsquares(1, 5): print(i, end=' ')

class SkipObject:
    def __init__(self, wrapped):  # Save item to be used
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)
class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped  # Iterator state information
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):  # Terminate iterations
            raise StopIteration

        else:
            item = self.wrapped[self.offset]  # else return and skip
            self.offset += 2
            return item
if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)  # Make container object
    I = iter(skipper)  # Make an iterator on it
    print(next(I), next(I), next(I))

    for x in skipper:  # for calls __iter__ automatically
        for y in skipper:  # Nested fors call __iter__ again each time
            print(x + y, end=' ')  # Each iterator has its own state, offset

# __iter__ + yield
class Squares: # __iter__ + yield generator
    def __init__(self, start, stop): # __next__ is automatic/implied
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2
for i in Squares(1, 5): print(i, end=' ')


# Multiple iterators with yield
class Squares:
    def __init__(self, start, stop):  # Non-yield generator
        self.start = start  # Multiscans: extra object
        self.stop = stop

    def __iter__(self):
        return SquaresIter(self.start, self.stop)
class SquaresIter:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

for i in Squares(1, 5): print(i, end=' ')

class SkipObject: # Another __iter__ + yield generator
    def __init__(self, wrapped):  # Instance scope retained normally
        self.wrapped = wrapped  # Local scope state saved auto

    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item


skipper = SkipObject('abcdefdedlepdlepdlep')
for x in skipper: # Each for calls __iter__: new auto generator
    for y in skipper:
        print(x + y, end=' ')



# Membership: __contains__, __iter__, and __getitem__
class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):  # Fallback for iteration
        print('get[%s]:' % i, end='')  # Also for index, slice
        return self.data[i]

    def __iter__(self):  # Preferred for iteration
        print('waht the fcuuk', end='')  # Allows only one active iterator
        self.ix = 0
        return self

    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, x):  # Preferred for 'in'
        print('contains: ', end='')
        return x in self.data
    next = __next__
if __name__ == '__main__':
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)  # call contains
    for i in X:  # for loops
        print(i, end=' | ')   # call iter
    print([i ** 2 for i in X]) # call iter
    print(list(map(bin, X)))
    I = iter(X)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration: break

# Attribute Access: __getattr__ and __setattr__

class Empty:
    def __getattr__(self, attrname): # On self.undefined
        if attrname == 'age':
            return 40
        else:
            raise AttributeError(attrname)
X = Empty()
print(X.age)

# Attribute Assignment and Deletion
class Accesscontrol:
    def __setattr__(self, attr, value):  # set attr
        if attr == 'age':
            self.__dict__[attr] = value + 10  # Not self.name=val or setattr
        else:
            raise AttributeError(attr + ' not allowed')
X = Accesscontrol()
X.age = 40
print(X.age)
