# read through file and print contents (line by line) all in upper case
fin = open('mbox-short.txt')
for line in fin:
    print(line.upper())
fin.close()