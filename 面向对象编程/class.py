

#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318645694388f1f10473d7f416e9291616be8367ab5000
#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的
#如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
class Student(object):
	#通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
	#__init__方法的第一个参数永远是self，表示创建的实例本身

	#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
	def __init__(self,name, score):
		self.__name=name
		self.__score=score
	#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
	def print_score(self):
		print('%s %s' %(self.__name,self.__score))
	def get_name(self):
		return self.__name
	def set_score(self,score):
		self.__score=score

#需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的
#不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量


bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)


#要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入

bart.print_score()
lisa.print_score()

#数据封装、继承和多态是面向对象的三大特点

bart.name = 'Bart Simpson'

#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：




#继承
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')


#当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。

c = Dog() # c是Dog类型
isinstance(c, Dog)
isinstance(c, Animal)


#只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

#对扩展开放：允许新增Animal子类；

#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。

#动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。