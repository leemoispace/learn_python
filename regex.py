'''

{n}表示n个字符，用{n,m}表示n~m个字符

    [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

    [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

    [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

    [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。

A|B可以匹配A或B，所以[P|p]ython可以匹配'Python'或者'python'。

^表示行的开头，^\d表示必须以数字开头。

$表示行的结束，\d$表示必须以数字结束。



'''



s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'
#因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：


#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。
import re

test = '010-123456'
if re.match(r'\d{3}\-\d{6}', test):
    print('ok')
else:
    print('failed')


#用正则表达式切分字符串
#\s可以匹配一个空格（也包括Tab等空白符
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))


 #提取子串
 #用()表示的就是要提取的分组（Group）。如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。比如：
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())



#编译
#如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

re_telephone.match('010-12345').groups()







import re
text = 'c++ python2 python3 perl ruby lua java javascript php4 php5 c'

#match,search,findall,split,sub
re.match(r'c++',text)
re.match(r'c\+\+',text)
re.match(r'java',text)
re.search(r'java',text)

print re.findall(r'python',text)
print re.split(r' perl ',text)
print re.sub(r'ruby','fortran',text)

# +   1-inf
# *   0-inf
# ?   0-1, 
# []  or
# {}  repeat
# [^] not
print re.findall(r'p+',text)
print re.findall(r'p[a-zA-Z]+',text)  #{1,}
print re.findall(r'c[a-zA-Z]*',text)  #{,inf}
print re.findall(r'c[^a-zA-Z]*',text)  #{,inf}
print re.findall(r'c[a-zA-Z]?',text)  #{,1}

# |   or
print re.findall(r'[pj][a-zA-Z]+',text)  #{,inf}
print re.findall(r'p[^0-9]+|j[a-zA-Z]+',text)   
print re.findall(r'p[^0-9 ]+|j[a-zA-Z]+',text) 

# ^   start
# $   end
# .   except \n
print re.findall(r'^c..',text)
print re.findall(r'c+',text)
print re.findall(r'c\++',text)
print re.findall(r'c$',text)

# \w  [a-zA-Z0-9_], \W
# \d  [0-9], \D
# \s  [ \t\n\r\f\v], \S
print re.findall(r'p\w+',text)
print re.findall(r'p\w+\d',text)
print re.findall(r'p\w+[0-9]',text)
print re.findall(r'p\w{5,9}',text)

# \b  word boundary
# \B  not \b
# \A  input start, ^
# \Z  input end, $
print re.findall(r'\bp[^0-9]',text)
print re.findall(r'p[^0-9]\b',text)

# *?  0~inf non-greedy
# +?  1~inf non-greedy
print re.findall(r'p[^0-9]*',text)
print re.findall(r'p[^0-9]*?',text)
print re.findall(r'p[^0-9]+\b',text)
print re.findall(r'p[^0-9]+?\b',text)

# ()  group
# (?P<name>pattern)
a=re.search(r'(p[a-zA-Z]+)([0-9])','python2')
print a.group(1), a.group(2)

a=re.search(r'(?P<name>p[a-zA-Z]+)(?P<version>[0-9])','python2')
print a.group('name'), a.group('version')
print a.groupdict()

pattern = re.compile(r'(?P<name>p[a-zA-Z]+)(?P<version>[0-9])')
results = pattern.search('python2')
print results.groupdict()
results = pattern.search('python3')
print results.groupdict()
results = pattern.search('php4')
print results.groupdict()

#########################################
for t in text.split(' '):
    results = pattern.search(t)
    if results:
      print results.groupdict()