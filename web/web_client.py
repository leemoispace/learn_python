import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Sarah']:
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()

'''
python 3 中的str 是unicode 字符串  b''表示是bytes   

str 转b''  可以用 encode('utf-8')  反转用 decode('utf-8')
'''