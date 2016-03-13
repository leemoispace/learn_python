# 其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。

import os
os.name
#环境变量，全部保存在os.environ这个变量中
os.environ.get('PATH')

'''
操作文件和目录的函数一部分放在os模块中，
一部分放在os.path模块中，这一点要注意一下。
查看、创建和删除目录可以这么调用：
'''
# 查看当前目录的绝对路径:
os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:'/Users/michael/testdir'
os.path.join('/Users/michael', 'testdir')

# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')


#把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符\/
#同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
os.path.split('/Users/michael/testdir/file.txt')


# os.path.splitext()可以直接让你得到文件扩展名('/path/to/file', '.txt')
os.path.splitext('/path/to/file.txt')

#这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作
os.rename('test.txt', 'test.py')
os.remove('test.py')

'''
但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。
幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
'''

#列出当前目录下os.listdir('.')的所有目录，只需要一行代码：
[x for x in os.listdir('.') if os.path.isdir(x)]

#列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']



'''

    利用os模块编写一个能实现dir -l输出的程序。

    编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。


dir -l :

# -*- coding: utf-8 -*-
import os
os.system('dir -l')

find:

# -*- coding: utf-8 -*-
import os
os.system('find . -name %s' % input('输入你要查询的关键字：\n'))
'''

