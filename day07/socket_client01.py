#Author:Bob

import socket

client = socket.socket()
client.connect(('localhost',9999))

while True:
    cmd = input(b'>>').strip()   #strip() 方法用于移除字符串头尾指定的字符（默认为空格）
    if len(cmd) == 0 :
        continue
    client.send(cmd.encode())
    cmd_res = client.recv(1024)

    print(cmd_res.decode())
socket.close()