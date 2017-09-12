#Author:Bob
#客户端
import socket
client = socket.socket()    #实例化socket
client.connect(('localhost',8888))
while True:
    msg = input('>>').strip().encode()
    if len(msg)==0:continue
    client.send(msg)
    data = client.recv(1024).decode()
    print('recv:',data)

client.close()

