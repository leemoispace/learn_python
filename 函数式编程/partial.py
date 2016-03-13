#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143184474383175eeea92a8b0439fab7b392a8a32f8fa000


#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
def int2_1(x, base=2):
    return int(x, base)


import functools
int2=functools.partial(int,base=16)#16 to 10

p=print
p(int2('1111111111'))


'''
创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
int2 = functools.partial(int, base=2)
实际上固定了int()函数的关键字参数base，也就是：
int2('10010')
相当于：
kw = { 'base': 2 }
int('10010', **kw)
'''
#实际上会把10作为*args的一部分自动加到左边,相当于：args = (10, 5, 6, 7)
max2 = functools.partial(max, 10)
p(max2(5, 6, 7))