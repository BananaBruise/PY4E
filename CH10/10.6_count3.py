import sys
sys.path.append('..')
from common.common import *
import string

fhand = open(ROMEO_FULL)
counts = dict()

# store word count in hashtable
for line in fhand:
    line = line.translate(str.maketrans('','',string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

# sort the dictionary by value
lst = list()
for key, val in counts.items():
    lst.append((val,key))

lst.sort(reverse=True)

for key, val in lst[:10]:
    print(key, val)