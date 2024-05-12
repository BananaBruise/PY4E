import sys
sys.path.append("..")
from common.common import *

fhand = open(MBOX_SHORT)
inp = fhand.read()
#total len of file
print(len(inp))
#first 20 char of file
print(inp[:20])