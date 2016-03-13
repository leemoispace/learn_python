#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431845183474e20ee7e7828b47f7b7607f2dc1e90dbb000

' a test module ' #任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'Michael Liao'
#以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。


import sys

def test():
    args = sys.argv
    #sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
  	#例如：运行python3 hello.py获得的sys.argv就是['hello.py']；
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__
if __name__=='__main__':
    test()
#而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码


