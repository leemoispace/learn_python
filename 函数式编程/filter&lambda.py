#和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，
#然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))

def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
#注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
#所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

#由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。



#lambda
g = lambda x : x**2
print g(4)

def f(x):
	return x**2
print f(4)





#prime number
#先构造一个从3开始的奇数序列：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列


# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


#请利用filter()滤掉非回数：
#return str(n)==str(n)[::-1]
def ispalindrome(n):
	n = str(n) 
	return n == n[::-1]#每向前取一个