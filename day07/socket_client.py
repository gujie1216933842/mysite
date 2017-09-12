__author__  = 'gujie'
#客户端
import  socket
client =  socket.socket();    #声明socket类型,同时生成socket连接对象
client.connect(('localhost',6969))
client.send('我爱你'.encode('utf-8'))   #传递中文
#client.send(b'dsafsef') 传英文
#注意bite类型只能接受ascll码的数据类型
#所以当你要传递中文,需要把信息encode(utf8)

data = client.recv(1024)
print('recv:',data.decode())
client.close()