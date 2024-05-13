import sys
sys.path.append('..')
from common.common import *
import re

fhand = open(MBOX)
fname = re.search(r'/([\w.]+)$', MBOX).group(1)

# count the lines that matches
count = 0
sum = 0
for line in fhand:
    lst = re.findall(r'New Revision: (\d+)$', line)
    if len(lst) > 0:
        sum += int(lst[0])
        count += 1

print(f'{fname} had average revision of {sum//count}')
