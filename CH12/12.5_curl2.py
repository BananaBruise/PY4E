import urllib.request as urlreq

# buffered read
img = urlreq.urlopen('http://data.pr4e.org/cover3.jpg')
fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break # no more data
    size = size + len(info)
    fhand.write(info)

print(size, 'characters copied')
fhand.close()