'''
http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143192607210600a668b5112e4a979dd20e4661cc9c97000#0
在程序运行的过程中，所有的变量都是在内存中
一旦程序结束，变量所占用的内存就被操作系统全部回收。
如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。

我们把变量从内存中变成可存储或传输的过程称之为序列化
在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

'''
#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
#或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
import pickle
d=dict(name='Bob',age=20,score=88)
pickle.dumps(d)

f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()

#当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
print(d)
'''
Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
'''

'''
 因为你把自己的源文件起名为json.py，“import json.py”实际上import的是你自己的代码。 
 '''


'''如果我们要在不同的编程语言之间传递对象，
就必须把对象序列化为标准格式，比如XML，
但更好的方法是序列化为JSON，
因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
'''

import json
d=dict(name='Bob', age=20, score=88)
#dumps()方法返回一个str，内容就是标准的JSON.类似的，dump()方法可以直接把JSON写入一个file-like Object。
print(json.dumps(d))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)



class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
#Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
print(json.dumps(s, default=student2dict))
#我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__))

#同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
#然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
