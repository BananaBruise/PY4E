import sys
sys.path.append("..")
from common.common import *

fhand = open(MBOX_SHORT)
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
            print(line)