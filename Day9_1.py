import time
import random

#题目1，2，3
def auth(func):
    print('Get in auth')
    def wrapper1(*args,**kwargs):
        name = input('user:>>')
        password = input('password:>>')
        if name == 'Albert' and password == '123':
            print('login successful')
            res = func(*args,**kwargs)
            return res
        else:
            print('login failes')
    return wrapper1




def timer(func):
    print('Get in timer')
    def wrapper(*args,**kwargs):
        start_time = time.time()
        print('start')
        res = func(*args,**kwargs)
        end_time = time.time()
        print('Run Time is %s'%(end_time-start_time))
        return res
    return wrapper


@timer
@auth
def foo():
    time.sleep(random.randint(2,9))
    print('Get in foo')

foo()



#
# 5 编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录
#
# 6 编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
#
# 7 为题目五编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，
# 否则，就去下载，然后存到文件中
# 扩展功能：用户可以选择缓存介质/缓存引擎，针对不同的url，缓存到不同的文件中
#
# 8 还记得我们用函数对象的概念，制作一个函数字典的操作吗，来来来，我们有更高大上的做法，
# 在文件开头声明一个空字典，然后在每个函数前加上装饰器，完成自动添加到字典的操作
#
# 9 编写日志装饰器，实现功能如：一旦函数f1执行，则将消息2017-07-21 11:12:11 f1 run写入到日志文件中，日志文件路径可以指定
# 注意：时间格式的获取
# import time
# time.strftime('%Y-%m-%d %X')
# 参考答案


# 题目4：
db='db.txt'
login_status={'user':None,'status':False}
def auth(auth_type='file'):
    def auth2(func):
        def wrapper(*args,**kwargs):
            if login_status['user'] and login_status['status']:
                return func(*args,**kwargs)
            if auth_type == 'file':
                with open(db,encoding='utf-8') as f:
                    dic=eval(f.read())
                name=input('username: ').strip()
                password=input('password: ').strip()
                if name in dic and password == dic[name]:
                    login_status['user']=name
                    login_status['status']=True
                    res=func(*args,**kwargs)
                    return res
                else:
                    print('username or password error')
            elif auth_type == 'sql':
                pass
            else:
                pass
        return wrapper
    return auth2

@auth()
def index():
    print('index')

@auth(auth_type='file')
def home(name):
    print('welcome %s to home' %name)


index()
home('albert')
#
# #题目五
import time,random
user={'user':None,'login_time':None,'timeout':0.000003,}

def auth(func):
    def wrapper(*args,**kwargs):
        if user['user']:
            timeout=time.time()-user['login_time']
            if timeout < user['timeout']:
                return func(*args,**kwargs)
        name=input('name>>: ').strip()
        password=input('password>>: ').strip()
        if name == 'albert' and password == '123':
            user['user']=name
            user['login_time']=time.time()
            res=func(*args,**kwargs)
            return res
    return wrapper

@auth
def index():
    time.sleep(random.randrange(3))
    print('welcome to index')

@auth
def home():
    time.sleep(random.randrange(3))
    print('welcome %s to home ')

index()
home('albert')
#
#
#题目6,7
import requests
import os
cache_file='cache.txt'
def make_cache(func):
    def wrapper(*args,**kwargs):
        if not os.path.exists(cache_file):
            with open(cache_file,'w'):pass

        if os.path.getsize(cache_file):
            with open(cache_file,'r',encoding='utf-8') as f:
                res=f.read()
        else:
            res=func(*args,**kwargs)
            with open(cache_file,'w',encoding='utf-8') as f:
                f.write(res)
        return res
    return wrapper

@make_cache
def get(url):
    return requests.get(url).text


res=get('https://www.python.org')

print(res)


# #题目八
route_dic={}

def make_route(name):
    def deco(func):
        route_dic[name]=func
    return deco
@make_route('select')
def func1():
    print('select')

@make_route('insert')
def func2():
    print('insert')

@make_route('update')
def func3():
    print('update')

@make_route('delete')
def func4():
    print('delete')

print(route_dic)
#
#
#题目九
import time
import os

def logger(logfile):
    def deco(func):
        if not os.path.exists(logfile):
            with open(logfile,'w'):pass

        def wrapper(*args,**kwargs):
            res=func(*args,**kwargs)
            with open(logfile,'a',encoding='utf-8') as f:
                f.write('%s %s run\n' %(time.strftime('%Y-%m-%d %X'),func.__name__))
            return res
        return wrapper
    return deco

@logger(logfile='aaaaaaaaaaaaaaaaaaaaa.log')
def index():
    print('index')
#
#index()