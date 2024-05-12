import sys
sys.path.append("..")
from common.common import *

fhand = open(MBOX_SHORT)
count = 0
for line in fhand:
    count = count + 1

print('Line count:',count)