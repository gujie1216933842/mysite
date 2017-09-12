#Author:Bob

#服务端socket

import socket

#实例化socket对象
server = socket.socket()
server.bind(('localhost',9999))
#监听
server.listen()
#接收客户端传来的数据

conn,adrr = server.accept()
data = conn.recv(1024)
print('recv:',data.decode())
conn.send(data.upper())
server.close()