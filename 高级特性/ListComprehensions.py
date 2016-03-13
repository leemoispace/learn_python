#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
list(range(1, 11))
print([x * x for x in range(1, 11)])
print([x*x for x in range(1,20) if x%2==0])

#生成全排列,两层循环
print([m+n for m in 'ABC' for n in 'XYZ'])
print([m+n+o for m in 'ABC' for n in 'XYZ' for o in '123'])

#列出当前目录下的所有文件和目录名
import os
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
	print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

#把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([n.lower() for n in L])