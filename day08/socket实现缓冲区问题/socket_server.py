__author__  = 'gujie'
#服务器端

import socket,os
server = socket.socket()
server.bind(('localhost',9999))
server.listen()
while True:
    conn,addr = server.accept()
    print('new conn:',addr)
    while True:
        print('接受新指令')
        data = conn.recv(1024)
        if not data:
            print('客户端已经断开')
            break
        print('执行指令:',data)
        cmd_res = os.popen(data.decode()).read()
        print('before send',len(cmd_res))
        if len(cmd_res) == 0:
            cmd_res = 'cmd has no output ....'
        conn.send(str(len(cmd_res.encode())).encode('utf-8'))   #先发数据大小给客户端
        conn.send(cmd_res.encode('utf-8'))

server.close()
