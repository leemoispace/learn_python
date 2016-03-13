class Student(object):
	def __init__(self, name):
		#实例属性
		self.name = name
	#直接在class中定义属性，这种属性是类属性，归Student类所有：这个属性虽然归类所有，但类的所有实例都可以访问到
	name='Student'

#相同名称的实例属性将屏蔽掉类属性