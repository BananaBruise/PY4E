'''
DSU pattern: sort a sequence by some "metadata" about the sequence itself
1. Decorate a sequence by building a list of tuples with one or more sort keys preceding the element from the sequence
2. Sort the list of tuples using the Python "sort"
3. Undecorate by extracting the sorted elemnts of the sequence
'''

txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
# decorate
for word in words:
    t.append((len(word), word))

# sort
t.sort(reverse=True)

# undecorate
res = list()
for length, word in t:
    res.append(word)

print(res)