import sys
sys.path.append('..')
from common.common import *

# create histogram of all emails from log
fhand = open(MBOX_SHORT)
emails = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        emails[words[1]] = emails.get(words[1],0) + 1

print(sorted(emails.items()))