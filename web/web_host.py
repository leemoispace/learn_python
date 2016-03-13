'''
服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，随后的通信就靠这个Socket连接了。

但是服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。

我们来编写一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。

'''
import socket ,threading,time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#然后，我们要绑定监听的地址和端口。

#服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，也可以用0.0.0.0绑定到所有的网络地址，还可以用127.0.0.1绑定到本机地址。
#端口号需要预先指定。因为我们写的这个服务不是标准服务，所以用9999这个端口号。请注意，小于1024的端口号必须要有管理员权限才能绑定：

#端口号需要预先指定
s.bind(('127.0.0.1',9999))
#调用listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
s.listen(5)
print('waiting for connection')

def tcplink(sock,addr):
	print('Accept new connection from %s:%s' %addr)
	sock.send(b'Welcome!')
	while True:
		data= sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':#如果客户端发送了exit字符串，就直接关闭连接。
			break
		sock.send(('Hwllo,%s!' %data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('connection from %s:%s closed!' %addr)



while True:
	#accept()会等待并返回一个客户端的连接:
	sock, addr = s.accept()
	#每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接：
	t=threading.Thread(target=tcplink,args=(sock,addr))
	t.start()


