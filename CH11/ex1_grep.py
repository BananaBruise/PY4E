import sys
sys.path.append('..')
from common.common import *
import re

fhand = open(MBOX)
fname = re.search(r'/([\w.]+)$', MBOX).group(1)

# get expression
regex = input("Enter a regular expression: ")

# count the lines that matches
count = 0
for line in fhand:
    if re.search(regex, line):
        count += 1

print(f'{fname} had {count} lines that matched {regex}')
