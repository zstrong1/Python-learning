# 1、自定义函数模拟range(1,7,2)
def my_range(start,stop,step):
    while start<stop:
        yield start
        start +=step
for k in my_range(1,7,2):
    print(k)
# 2、模拟管道，实现功能:tail -f access.log | grep '404'
import time
def tail(filepath):
    with open(filepath,'rb') as f:
        f.seek(0,2)
        while True:
            line=f.readline()
            if line:
                yield line
            else:
                time.sleep(0.2)

def grep(pattern,lines):
    for line in lines:
        line=line.decode('utf-8')
        if pattern in line:
            yield line

for line in grep('404',tail('access.log')):
    print(line,end='')

#测试
with open('access.log','a',encoding='utf-8') as f:
    f.write('出错啦404\n')

# 3、编写装饰器，实现初始化协程函数的功能
#
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper
@init
def eater(name):
    print('%s 准备开始吃饭啦' %name)
    food_list=[]
    while True:
        food=yield food_list
        print('%s 吃了 %s' % (name,food))
        food_list.append(food)

g=eater('albert')
g.send('蒸羊羔')
# 4、实现功能：grep  -rl  'python'  /etc
#题目四：
#注意：target.send(...)在拿到target的返回值后才算执行结束
import os
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper

@init
def search(target):
    while True:
        filepath=yield
        g=os.walk(filepath)
        for dirname,_,files in g:
            for file in files:
                abs_path=r'%s\%s' %(dirname,file)
                target.send(abs_path)
@init
def opener(target):
    while True:
        abs_path=yield
        with open(abs_path,'rb') as f:
            target.send((f,abs_path))
@init
def cat(target):
    while True:
        f,abs_path=yield
        for line in f:
            res=target.send((line,abs_path))
            if res:
                break
@init
def grep(pattern,target):
    tag=False
    while True:
        line,abs_path=yield tag
        tag=False
        if pattern.encode('utf-8') in line:
            target.send(abs_path)
            tag=True
@init
def printer():
    while True:
        abs_path=yield
        print(abs_path)


g=search(opener(cat(grep('你好',printer()))))
# g.send(r'E:\CMS\aaa\db')
g=search(opener(cat(grep('python',printer()))))
g.send(r'E:\CMS\aaa\db')
# 5、Python语言 实现八皇后问题

