import urllib.request as urlreq

try:
    url = input("Enter url: ")
    fhand = urlreq.urlopen(f'http://{url}')
except:
    print('bad url')
    exit(1)

# retrive up to 3k char
content = fhand.read(3000).decode()

# show first 3k content and count total number of char
print(content)
print(f'number of character read {len(content)}')
