import sys
sys.path.append('..')
from common.common import *

fhand = open(MBOX_SHORT)
result = dict()
for line in fhand:
    words = line.split()
    if len(words) > 3 and line.startswith('From '):
        result[words[2].capitalize()] = result.get(words[2].capitalize(),0) + 1

print(result)