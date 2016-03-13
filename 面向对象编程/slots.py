#当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。
class Student(object):
	#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
	__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
	#__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
	#slots只能限制添加属性，不能限制通过添加方法来添加属性：

s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age): # 定义一个函数作为实例方法
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
#给一个实例绑定的方法，对另一个实例是不起作用的：
#为了给所有实例都绑定方法，可以给class绑定方法：

def set_score(self, score):
	self.score = score

Student.set_score = MethodType(set_score, Student)
#动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

