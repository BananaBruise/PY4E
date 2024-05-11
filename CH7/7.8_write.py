# write file
fout = open('output.txt','w')
line1 = 'This here\'s the wattle\n'
line2 = 'the amblem of our land.\n'
fout.write(line1)
fout.write(line2)
fout.close()

# read back and confirm
fin = open('output.txt','r')
if fin.readline() != line1:
    print('line1 mismatch')
    exit(1)
if fin.readline() != line2:
    print('line2 mismatch')
    exit(1)
print('file matches!')
fin.close()


