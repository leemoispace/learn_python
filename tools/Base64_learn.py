'''
让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。
Base64是一种最常见的二进制编码方法。

3 bytes to 4 parts 
Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

'''
累了
#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431954588961d6b6f51000ca4279a3415ce14ed9d709000#0











a = (-len(s)) % 4
s=s+b'='*a
return base64.b64decode(s)