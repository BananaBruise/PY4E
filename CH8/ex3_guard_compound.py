import sys
sys.path.append('..')
from common.common import *

fhand = open(MBOX_SHORT)
count = 0
for line in fhand:
    words = line.split()
    # use compound logical expression
    if len(words) <= 3 or words[0] != 'From': continue
    print(words[2])