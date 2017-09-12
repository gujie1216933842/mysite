#Author:Bob

import socket

client = socket.socket()   #实例化socket对象
client.connect(('localhost',9999))  #连接服务端

client.send('我爱你A'.encode('utf-8'))

data = client.recv(1024)   #客户端接收的数据大小
print('recv:',data.decode())



