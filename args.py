#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000
#默认参数
def power(x, n=2):#必选参数在前，默认参数在后,把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


#默认参数有个最大的坑:默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L
add_end()
add_end()
print(add_end())


def add_end2(L=None):
    if L is None:#None这个不变对象,无论调用多少次，都不会有问题：
        L = []
    L.append('END')
    return L


    #可变参数
def calc(*numbers):#在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
print(calc(*nums))#*nums表示把nums这个list的所有元素作为可变参数传进去

#关键字参数:**
#允许你传入0个或任意个含参数名的参数
#这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Adam', 45, gender='M', job='Engineer')

#先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)


#命名关键字参数，
#例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    print(name, age, city, job)

person('Jack', 24, city='Beijing', job='Engineer')

#必选参数、默认参数、可变参数、关键字参数和命名关键字参数:5种参数都可以组合使用
#参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数。