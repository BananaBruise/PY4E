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

# search for most email count
max_email = ''
max_count = 0
for k,v in emails.items():
    if v > max_count:
        max_email = k
        max_count = v

print(max_email,max_count)