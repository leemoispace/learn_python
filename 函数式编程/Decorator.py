def now():
	print('2015.8.11')

f=now
p=print

#函数对象有一个__name__属性，可以拿到函数的名字：
p(f.__name__)



#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
#这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

def log(func):
	def wrapper(*args, **kw):#wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用
		p('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper
#上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
#借助Python的@语法，把decorator置于函数的定义处

@log
def now():
#上面的log，因为它是一个decorator，所以接受一个函数作为参数，
    print('2015-3-25')

#调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：

now()
#把@log放到now()函数的定义处，相当于执行了语句：now = log(now)


#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

#3层嵌套的效果是这样的：>>> now = log('execute')(now)
#首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
now()

#经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
p(now.__name__)
#需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。


#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper



#写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
def forwardcall(func):
    def wrapper(*args, **kw):
        print("begin call")
        return func(*args, **kw)
    return wrapper

@forwardcall
def now(func):
    print("我才是主要逻辑所在。")
    def wrapper(*args, **kw):
        return func(*args, **kw)
    return wrapper


@now
def endcall():
    print("end call")

#大致思路是A装饰B,B装饰C，B是指定函数，A是执行前打印日志，C是执行后打印日志——倒推
endcall()