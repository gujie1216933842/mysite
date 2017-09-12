#Author:Bob

import socket

client = socket.socket()
client.connect(('localhost',9999))

msg = input('>>').strip()

client.send(msg.encode())

data = client.recv(1024)

print('recv:',data.decode())

client.close()