import sys
sys.path.append('..')
from common.common import *

fhand = open(MBOX_SHORT)
f_count = 0

for line in fhand:
    words = line.split()
    if len(words) < 2 or not line.startswith('From '): continue
    f_count += 1
    print(words[1])

print("There were",f_count,"lines in the file with From as the first word")