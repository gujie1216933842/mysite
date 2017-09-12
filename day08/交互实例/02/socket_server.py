#Author:Bob

#服务器端
import socket
server = socket.socket()
# 绑定
server.bind(('localhost',9999))
# 监听
server.listen()
# 等待电话呼入
conn,adrr = server.accept()
# 接收信息
data = conn.recv(1024)
print('recv:',data.decode())
# 给客户端返回信息
conn.send(data)  #往客户端返回数据

server.close()