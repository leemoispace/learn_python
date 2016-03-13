'''
http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431955007656a66f831e208e4c189b8a9e9f3f25ba53000
https://docs.python.org/3/library/struct.html#format-characters


在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。

在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：



Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
'''


import struct
struct.pack('>I',10240099)
#pack的第一个参数是处理指令，'>I'的意思是：>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。

struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
#根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。



