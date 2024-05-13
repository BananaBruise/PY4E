import socket
import time

# prompt for user supplied URL
url = input ("url: ")
hostname = url.split('/')[0]
# create socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((hostname, 80))
    # send command over socket
    cmd = f'GET http://{url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
except:
    print('cannot connect')
    exit()

# get response
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break # read until socket is empty
    time.sleep(0.25)
    print(data.decode(),end='')

mysock.close()

