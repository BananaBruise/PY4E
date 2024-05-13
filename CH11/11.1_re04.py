# Search for lines that start with From and have an at sign
import re
import sys
sys.path.append('..')
from common.common import *

fhand = open(MBOX_SHORT)
for line in fhand:
    line = line.rstrip()
    if re.search('From:.+@', line): # match any user with email (but must have user)
        print(line)