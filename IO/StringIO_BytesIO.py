#很多时候，数据读写不一定是文件，也可以在内存中读写。.
#StringIO顾名思义就是在内存中读写str。


from io import StringIO
f = StringIO()
f.write('hello')
f.write('world!')


print(f.getvalue())

h = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s=h.readline()
	if s=='':
		break
	print(s.strip())


#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))

#请注意，写入的不是str，而是经过UTF-8编码的bytes。
print(f.getvalue())
#用一个bytes初始化BytesIO，然后，像读文件一样读取
h = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(h.getvalue())