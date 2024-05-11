fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print("bad file name")
    exit()

count = 0
conf = 0.0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        index = line.find(': ')
        conf += float(line[index+1:-1])
        count += 1

print('Average spam confidence:',round(conf/count,4))