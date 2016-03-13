#type()函数返回的是什么类型呢？它返回对应的Class类型
type(123)
type(abs)

import types
def fn():
	pass

type(fn)==types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType
type((x for x in range(10)))==types.GeneratorType



#能用type()判断的基本类型也可以用isinstance()判断：
isinstance(123, int)
isinstance(b'a', bytes)
#并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
isinstance((1, 2, 3), (list, tuple))

#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
dir('ABC')
#如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法
#下面的代码是等价的：
len('ABC')
'ABC'.__len__()



#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
obj = MyObject()
hasattr(obj, 'x') # 有属性'x'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
getattr(obj, 'y') # 获取属性'y'

getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
fn()# 调用fn()与调用obj.power()是一样的