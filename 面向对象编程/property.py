#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143186781871161bc8d6497004764b398401a401d4cce000#0


class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

        #但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？

#还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。


class Student(object):

    @property#把一个getter方法变成属性，只需要加上@property就可以了，
    def score(self):
        return self._score

    @score.setter#此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


#只定义getter方法，不定义setter方法就是一个只读属性：
#birth是可读写属性，而age就是一个只读属性
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth


s=Student()
s.score=9999#实际转化为s.set_score(9999)


#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。


#请利用@property给一个Screen对象加上width和height属性，
#以及一个只读属性resolution：

class Screen(object):
	def __init__(self):
		self.__width=1280
		self.__height=768
		self.resolution=1280*768

	@property 
	def resolution(self):
		return self.__resolution

	@property
	def width(self):
		return self.__width

	@width.setter
	def width(self,value):
		self.__width=value
		self.resolution=self.width*self.height 

	@property
	def height(self):
		return self.__height
	@height.setter
	def height(self,value):
		self.__height=value
		self.resolution=self.width*self.height 
		



