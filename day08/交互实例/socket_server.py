#Author:Bob
#服务器端
import socket
server = socket.socket()
server.bind(('localhost',9999))
server.listen()  #监听
conn,adrr = server.accept()  #等待人家把数据发过来 ,返回两个标记值,conn就是客户端连过来而在服务器端为其生成的一个连接实例

data = conn.recv(1024)  #接收客户端发来的信息
print('recv:',data)

conn.send(data.upper())
server.close()