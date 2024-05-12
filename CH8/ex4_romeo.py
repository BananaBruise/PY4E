import sys
sys.path.append('..')
from common.common import *

fin = open(ROMEO)
u_words = []

# find unique words
for line in fin:
    words = line.split()
    for word in words:
        if word in u_words: continue
        u_words.append(word)

# print sorted unique words
u_words.sort()
print(u_words)