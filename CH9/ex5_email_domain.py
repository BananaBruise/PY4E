import sys
sys.path.append('..')
from common.common import *

# create histogram of email domain
fhand = open(MBOX_SHORT)
emails = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        domain = words[1].split('@')[1]
        emails[domain] = emails.get(domain,0) + 1

print(emails)