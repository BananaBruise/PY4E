import sys
sys.path.append('..')
from common.common import *

fhand = open(MBOX_SHORT)

# parse "From " line and pull out address & count
mail_counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        mail_counts[words[1]] = mail_counts.get(words[1],0) + 1

# sort number email by count (using DSU - decorate, sort, undecorate)
sorter = [(v,k) for k,v in mail_counts.items()]
sorter.sort(reverse=True)

# print most sent email
print(sorter[0][1], sorter[0][0]) # email, count