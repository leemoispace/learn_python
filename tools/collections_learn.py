'''collections是Python内建的一个集合模块，提供了许多有用的集合类。'''

#namedtuple
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(2,1)
print(p.x,p.y)

#deque
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')


#defaultdict
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key2'])
#除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。


#OrderedDict
#如果要保持Key的顺序，可以用OrderedDict：会按照插入的顺序排列，不是Key本身排序：
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d ,'dict的Key是无序的')
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od ,'ordereddict的Key是无序的')

#可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


#Counter
from collections import Counter
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)
