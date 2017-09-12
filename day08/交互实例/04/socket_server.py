#Author:Bob

import socket

server = socket.socket()
server.bind(('localhost',9999))

server.listen()
print('等待接电话')
while True:
    conn,adrr = server.accept()
    print('开始接电话')
    while True:
        data = conn.recv(1024)
        print('recv:', data.decode())
        if not data:
            print('client has lost...')
            break
        conn.send(data)

server.close()
