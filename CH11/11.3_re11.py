# capture group using findall()

import re
import sys
sys.path.append('..')
from common.common import *

fhand = open(MBOX_SHORT)
for line in fhand:
    line = line.rstrip()
    x = re.findall('^X-\S*: ([0-9.]+)', line)
    if len(x) > 0:
        print(x)