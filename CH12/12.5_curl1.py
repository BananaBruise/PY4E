import urllib.request as urlreq

img = urlreq.urlopen('http://data.pr4e.org/cover3.jpg').read()
fhand = open('cover3.jpg','wb')
fhand.write(img)
fhand.close()
