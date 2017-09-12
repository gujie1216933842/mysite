#Author:Bob
import socket

client =  socket.socket()
client.connect(('localhost',9999))  #参数为一个元组
client.send(b'ddd!')

data = client.recv(1024)
print('recv:',data)

client.close()