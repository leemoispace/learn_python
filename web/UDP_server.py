'''
使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。


'''

import socket 
#SOCK_DGRAM指定了这个Socket的类型是UDP。
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


s.bind(('127.0.0.1',9999))
#绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：

print('Bind UDP on 9999...')
#注意这里省掉了多线程，因为这个例子很简单。
while True:
	#recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。
	data,addr=s.recvfrom(1024)
	print('Receive form %s:%s.' %addr)
	#s.sendto(b'Hello,%s!' %data,addr)
	s.sendto(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'), addr)

