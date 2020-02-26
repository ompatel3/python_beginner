# Learning python 5e page 387
# CHAPTER 13 while and for Loops
x = 'spam'
while x: # While x is not empty
    print(x, end=' ') # In 2.X use print x,
    x = x[1:] # Strip first character off x
a=0; b=10
while a < b: # One way to code counter loops
    print(a, end=' ')
    a += 1 # Or, a = a + 1


# continue
x = 10
while x:
    x -= 1
    if x % 2 != 0: continue # Odd? -- skip print
    print(x, end=' ')
x = 10
while x:
    x = x-1
    if x % 2 == 0: print(x, end=' ')


# break
while True:
    name = input('Enter name:')
    if name == 'stop': break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age) ** 2)


# loop else
y = 189992
x = y // 2 # For some y > 1
while x > 1:
    if y % x == 0: # Remainder
        print(y, 'has factor', x)
        break # end while loop
    x -= 1
else:
    print(y, 'is prime')


y = 189992
x = y // 2 # For some y > 1
while x > 1:
    if y % x == 0: # Remainder
        print(y, 'has factor', x)
    x -= 1
else:
    print(y, 'is prime')

more on loop else  find int in x
x = ["2pam","dwdw","ddd","2",2,100]
found = False
while x and not found:
    if isinstance(x[0], int):
        print('Ni')
        found = True
    else: x = x[1:] # Slice off front and repeat
if not found:
    print('not found')

while x: # Exit when x empty
     if isinstance(x[0], int):
        print('Ni')
     break # Exit, go around else
     x = x[1:]
else:
     print('Not found') # Only here if exhausted x

