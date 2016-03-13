#取一个list或tuple的部分元素
#对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])#直到索引3为止，但不包括索引3
print(L[:3])
L = list(range(100))
L[::5]


#tuple
print((0, 1, 2, 3, 4, 5)[:3])
#字符串,like substring
'ABCDEFG'[:3]