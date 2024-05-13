import sys
sys.path.append('..')
from common.common import *

fhand = open(MBOX)

# collect alpha & frequency into hashtable
letters = dict()
l_count = 0.0; # number of alpha seen
for line in fhand:
    for char in line:
        if char.isalpha():
            c = char.lower()
            # store into hashtable
            letters[c] = letters.get(c,0) + 1
            l_count +=1

# replace list with frequency (instead of count)
l_freq = [(k,round(v/l_count * 100, 2)) for k,v in letters.items()]

# sort by frequency
l_freq.sort(key = lambda x: x[1], reverse=True)

# print output
print('letter | frequency')
for letter, freq in l_freq:
    print(f'{letter} | {freq}%')


