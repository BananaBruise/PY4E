# store words as key in dictionary
# note: in this implementation, value is the order the words was added

import sys
sys.path.append('..')
from common.common import *

fhand = open(WORDS)
word_bank = dict()
seen_counter = 1
for line in fhand:
    words = line.split()
    for word in words:
        if word in word_bank: continue
        word_bank[word] = seen_counter
        seen_counter += 1

print(sorted(word_bank.items()))
