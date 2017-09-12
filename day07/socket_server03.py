#Author:Bob

import socket,os
server = socket.socket()   #实例化socket
server.bind(('localhost',9999))  #绑定服务器
server.listen()   #socket监听

#一层循环
while True:
    conn,adrr = server.accept()   #接收客户端发来的信息,信息中有两个变量
    print('new conn',adrr)        #把新连接打印出来
    #里面一层小循环
    while True:
        data = conn.recv(1024)    #接收信息,赋值给data
        if not data:
            print('客户端已经断开')  #判断是否有数据,如果没有,显示客户端已经断开
            break                   #结束循环
        cmd_res = os.popen(data.decode()).read()  #os系统读取客户端传来的命令
        # print(cmd_res)
        if len(cmd_res)==0:
            cmd_res = "cmd has no output..."
        conn.send(cmd_res.encode())               #os返回结果
        print(cmd_res)
socket.close()

