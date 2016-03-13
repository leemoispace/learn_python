sorted([36, 5, -12, 9, -21])

#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
sorted([36, 5, -12, 9, -21], key=abs)

#忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

sorted(L,key=lambda x : x[0].lower())

sorted(L,key=lambda x : x[1],reverse=True)