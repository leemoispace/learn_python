'''
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，
执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
'''
try:
	print('try')
	r=10/0
	print('result:',r)

except ZeroDivisionError as e:
	print('except:', e)
else:  #此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
	pass
finally:
	print('finally')
print('END')


try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')


'''
Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。

Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：https://docs.python.org/3/library/exceptions.html#exception-hierarchy


如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。




def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()
'''

'''
记录错误

如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

'''

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')




'''
如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
