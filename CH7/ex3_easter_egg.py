fname = input('Enter the file name: ').strip()
# easter egg
if fname.lower() == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    exit(0)

try:
    fhand = open(fname)
except:
    print('File cannot be opened:',fname)
    exit(1)

# count number of lines
count = 0
line = fhand.readline()
while line:
    if line.startswith('Subject:'):
        count += 1
    line = fhand.readline()

print('There were',count,'subject lines in',fname)
