'''class Persion():
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def greet(self):
        print('hello,world! I am {}.'.format(self.name))

foo=Persion()
bar=Persion()
foo.set_name('刘慷')
bar.set_name('wenhua')
print(foo.greet())
print(bar.greet())'''
'''class Filter:
    def init(self):
        self.blocked=[]
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]
class sonfilter(Filter):
    def init(self):
        self.blocked=['son']
f=Filter()
f.init()
print(f.filter([1,2,3]))
s=sonfilter()
s.init()
f=s.filter(['son','som','son','zhangsan','sun','egg'])
print(f)
print(issubclass(sonfilter,Filter))
print(issubclass(Filter,sonfilter))
print(sonfilter.__bases__)
print(Filter.__bases__)
# from abc import ABC,abstractmethod
try:
    x=int(input('enter a number:'))
    y=int(input('enter a number:'))
    print(x/y)
# except ZeroDivisionError:
except Exception as msg:
    print(msg)
else:
    print('you are smart,fly high:',x/y)
finally:
    print('done')'''
'''lass Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('I am hungry')
            self.hungry=False
        else:
            print('No,thanks')
class SongBird(Bird):
    def __init__(self):
        # Bird.__init__(self)
        super().__init__()
        self.sound='you are very good'
    def sing(self):
        print(self.sound)
a=SongBird()
sb=a.sing()
sd=a.eat()
print(sb)
print(sd)'''
# 创建一个无穷序列
def check_index(key):
    if not isinstance(key,int):
        raise TypeError
    if key<0:
        raise IndexError
class AiritmeticSequence:
    def __init__(self,start=0,step=1):
        self.start=start
        self.step=step
        self.change={}
    def __getitem__(self, key):
        check_index(key)
        try:
            return self.change[key]
        except KeyError:
            return self.start+key*self.step
    def __setitem__(self, key, value):
        check_index(key)
        self.change[key]=value
s=AiritmeticSequence(1,2)
print(s[4])
s[4]=2
print(s[4])
print(s[5])
# 带访问计数器的列表
class CounterList(list):
    def __init__(self,*args):
        super().__init__(*args)
        self.counter=0
    def __getitem__(self, index):
        self.counter+=1
        return super(CounterList,self).__getitem__(index)
cl=CounterList(range(10))
print(cl)
cl.reverse()
print(cl)
# 迭代器斐波那契数
class Fibs:
    def __init__(self):
        self.a=0
        self.b=1
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self
b=Fibs()
for f in b:
    if f>10:
        print(f)
        break
it=iter([1,2,3])
print(next(it))
# pprint来玩一把
import sys,pprint
pprint.pprint(sys.path)
print(range.__doc__)
print(set(range(10)))
# 读写文件
f=open(r'C:\Apps\liukang.txt','w')
f.write('''未来已经来了，我还能干什么，如果大海能够带走我的爱，\n我多希望你能明白
,原来我是如何爱你的，怎么会把自己忘了，为什么会这样，我该如何去追求呢，
天下为公，一辈子只追寻一个人就够了''')
print(f.seek(5))
f.close()
f=open(r'C:\Apps\liukang.txt')
print(f.read())
print(f.tell())
f.close()
# readline读取liukang.txt
f=open(r'C:\Apps\liukang.txt')
for  i in range (4):
    print(str(i)+':'+f.readline(),end='')
f.close()
# 使用with
with open(r'C:\Apps\liukang.txt','w') as liu:
    liu.write('爱一个人真的很难，我们该如何面对，怎么去杀人')

# python的GUI图像
import tkinter as tk
from tkinter import *
top=tk()
mainloop()



