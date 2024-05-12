t = ['a','b','c']

# append = add single item to end of list
t.append('d')
print(t)

# extend = "append all"
t2 = ['d','e']
t.extend(t2)
print(t)

# sort
t.sort(reverse=True) # reverse sort
print(t)