# search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'

import re
import sys
sys.path.append('..')
from common.common import *

fhand = open(MBOX_SHORT)
for line in fhand:
    line = line.rstrip()
    if re.search('F..m:', line):
        print(line)