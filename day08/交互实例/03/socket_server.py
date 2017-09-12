#Author:Bob

#服务端socket

import socket
server = socket.socket()
server.bind(('localhost',8888))

server.listen()

conn,adrr = server.accept()
print('开始等电话')
while True:

    data = conn.recv(1024)
    print('recv:',data)
    conn.send(data)



server.close()


