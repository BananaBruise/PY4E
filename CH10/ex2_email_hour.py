import sys
sys.path.append('..')
from common.common import *

fhand = open(MBOX_SHORT)

# parse "From " line and pull out hour & count
mail_counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        hour = words[5].split(':')[0]
        mail_counts[hour] = mail_counts.get(hour,0) + 1

# sort by hour
sorter = [(k,v) for k,v in mail_counts.items()]
sorter.sort()

# print result
for hour, count in sorter:
    print(hour, count)