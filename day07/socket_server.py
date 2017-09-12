__author__  = 'gujie'
#服务器端
import  socket
server = socket.socket();
server.bind(('localhost',6969))   #绑定要监听端口
server.listen()   #监听

print('电话来了')
conn,adrr = server.accept()  #等电话打进来  //python3里只能发bite比特流的bite类型
print(conn,adrr)
#conn就是客户端连过来而在服务器端为其生成的一个连接实例(重点)

print('我要接电话了')
data = conn.recv(1024)  #等电话打进来  //python3里只能发bite比特流的biye类型
print('recv:',data)
conn.send(data.upper())
server.close()
	