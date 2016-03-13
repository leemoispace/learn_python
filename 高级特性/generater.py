#那我们是否可以在循环的过程中不断推算出后续的元素呢？
#这样就不必创建完整的list，从而节省大量的空间。
#在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * x for x in range(10))
print(g)
print(next(g))
#每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素
for n in g:
	print(n)


#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
#在执行过程中，遇到yield就中断，下次又继续执行。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b# print(b) #断点
        a, b = b, a + b
        n = n + 1
    return 'done'

f=fib(10)
for i in f:
	print(i)

#generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。

#杨辉三角?
def triangles():
	L=[1]
	while(True):
		yield L
		L=[1]+[L[n]+L[n+1] for n in range(len(L)-1)]+[1];

'''
t=triangles(10)
for i in t:
	print(i)
'''

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter('abc'), Iterator)
#Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#凡是可作用于for循环的对象都是Iterable类型；凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；