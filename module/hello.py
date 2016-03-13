#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module ' #任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'Michael Liao'
#以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。


import sys

def test():
    args = sys.argv
    #sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
        if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()