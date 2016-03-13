import pdb

s = '0'
n = int(s)
print 10 / n
'''

$ python3 -m pdb err.py
以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码

输入命令l来查看代码：
输入命令n可以单步执行代码：
任何时候都可以输入命令p 变量名来查看变量：
输入命令q结束调试，退出程序：

'''


'''
这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：
'''

import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停,用命令c继续运行：
print 10 / n
