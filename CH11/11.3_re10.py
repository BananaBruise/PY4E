# search for 'X-' line and has a decimal value

import re
import sys
sys.path.append('..')
from common.common import *

fhand = open(MBOX_SHORT)
for line in fhand:
    line = line.rstrip()
    if re.search('^X-\S*: [0-9.]+', line):
        print(line)