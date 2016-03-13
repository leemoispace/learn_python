#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print('hello,world!')
#name=input()
#print(name)
print(r'\\\t\\')

print('''line1
... line2
... line3''')


#Unicode
print('包含中文的str')

print(ord('A'))
print(chr(ord('A')))

print('\u4e2d\u6587')
print('中文'.encode('utf-8'))
print( b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))



print('Hi, %s, you have $%d.' % ('Michael', 1000000))
#为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。


#list
classmates=['lee','wang','zhang']

len(classmates)

classmates[-1]
classmates.append('adam')

classmates.insert(1,'jack')
classmates.pop()
classmates.pop(2)

L=['aoole',2,True]

s = ['python', 'java', ['asp', 'php'], 'scheme']

#tuple和list非常类似，但是tuple一旦初始化就不能修改(tuple的每个元素，指向永远不变)
classmates_tuple= ('Michael', 'Bob', 'Tracy')
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)

"""
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
"""

bmi =30
if bmi>32:
	print('严重肥胖')
elif bmi>28:
	print('fat')

for name in classmates:
	print(name)


#for
sum=0
for x in range(101):
	sum=sum+x
print(sum)

#while
sum=0
n=99
while n>0:
	sum=sum+n
	n-=2
print(sum)


#dict----在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。
#需要占用大量的内存，内存浪费多。
#dict的key必须是不可变对象。通过key计算位置的算法称为哈希算法（Hash）。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#in
if 'Thomas' in d:
	print('thomas in d')
else:
	print('Thomas not in d')

#get方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas','Thomas not in d'))

d.pop('Bob')



#set:集合不能重复,无序.
#set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象
s = set([1, 2, 3])
s.add(4)
s.remove(4)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
s1 & s2
s1 | s2

#str是不变对象，而list是可变对象。key不变对象

abs(-100)
max(1,2,3,5)
a=abs
a(-1)

print(hex(255))



def myabs(x):
	if x>=0:
		return x
	else:
		return -x
#参数检查
def my_abs(x):
    if not isinstance(x, (int, float)):#数据类型检查
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#函数可以同时返回多个值，但其实就是一个tuple。
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)

print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)

def quadratic(a,b,c):
	delta=b*b-4*a*c
	if delta>=0:
		x1=(-b+math.sqrt(delta))/(2*a)
		x2=(-b-math.sqrt(delta))/(2*a)
		return x1,x2
	else:
		return 'error'

print(quadratic(2,4,1))



'''
安装module：
$ pip3 install mysql-connector-python --allow-external mysql-connector-python -i http://pypi.v2ex.com/simple
'''
