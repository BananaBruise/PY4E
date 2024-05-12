import sys
sys.path.append("..")
from common.common import *

# read through file and print contents (line by line) all in upper case
fin = open(MBOX_SHORT)
for line in fin:
    print(line.upper())
fin.close()