#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431835236741e42daf5af6514f1a8917b8aaadff31bf000

#可变参数的求和
def calc_sum(*args):
	ax=0
	for n in args:
		ax=ax+n
	return ax

#不需要立刻求和
#不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum

f=lazy_sum(1,2,3,4,5,6,6)
#调用函数f时，才真正计算求和的结果：
f()

#在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
#这种称为“闭包（Closure）”的程序结构拥有极大的威力。



def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3=count()
f1()
f2()
f3()
#返回闭包时牢记的一点就是：
#返回函数不要引用任何循环变量(i)，或者后续会发生变化的变量。


#如果一定要引用循环变量怎么办？方法是再创建一个函数(g)，用该函数的参数绑定循环变量当前的值，
#无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count2():
	def f(j):
		def g():
			return j*j
		return g
	fs=[]
	for i in range(1,4):
		fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
	return fs