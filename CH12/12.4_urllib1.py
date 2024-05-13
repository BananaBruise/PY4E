import urllib.request as urlreq

# treat web content like a file
fhand = urlreq.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())