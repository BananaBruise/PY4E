import sys
sys.path.append("..")
from common.common import *

fhand = open(MBOX_SHORT)
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)