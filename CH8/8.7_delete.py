t = ['a','b','c']

# pop - returns nth item removed (default to last)
x = t.pop(1)
print(t)
print(x)

# del keyword - does nth value without return value
t = ['a','b','c']
del t[1]
print(t)

# del with slice
t = ['a','b','c','d','e','f']
del t[1:5]
print(t)

# remove - deletion by value (no return)
t = ['a','b','c']
t.remove('b')
print(t)
