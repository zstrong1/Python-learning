# 写代码,有如下变量,请按照要求实现每个功能 （共6分，每小题各0.5分）
name = " alberT"
# 1)    移除 name 变量对应的值两边的空格,并输出处理结果
print(name.strip())
# 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果 
print(name.startswith('al'))
# 3)    判断 name 变量对应的值是否以 "T" 结尾,并输出结果 
print(name.endswith('T'))
# 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
print(name.replace('l','p'))
# 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
print(name.split('l'))
# 6)    将 name 变量对应的值变大写,并输出结果 
print(name.upper())
# 7)    将 name 变量对应的值变小写,并输出结果 
print(name.lower())
# 8)    请输出 name 变量对应的值的第 2 个字符?
print(name[1])
# 9)    请输出 name 变量对应的值的前 3 个字符?
print(name[-2:])
# 10)    请输出 name 变量对应的值的后 2 个字符? 
print(name.find('e'))
# 11)    请输出 name 变量对应的值中 “e” 所在索引位置? 
print(name[:-1])
# 12)    获取子序列,去掉最后一个字符。如: albert 则获取 alber


# 有列表data=['albert',18,[2000,1,1]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量
data = ['albert',18,[2000,1,1]]
name = data[0]
print(name)
age = data[1]
print(age)
birthday = data[2]
print(birthday)


"""简单购物车,要求如下：
实现打印商品详细信息，用户输入商品名和购买个数，则将商品名，价格，购买个数加入购物列表，如果输入为空或其他非法输入则要求用户重新输入
"""
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
goods_l=[]
Tag = 4
while 0:
    for key,item in msg_dic.items():
        print('name:{name} price:{price}'.format(price=item,name=key))
    choice=input('商品>>: ').strip()
    if not choice or choice not in msg_dic:continue
    count=input('购买个数>>: ').strip()
    if not count.isdigit():continue
    goods_l.append((choice,msg_dic[choice],count))

    print(goods_l)


"""
有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中
即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
"""
number = {'k1':[],'k2':[]}
c = [11,22,33,44,55,66,77,88,99,90]
for i in c:
    if i >66:
        number['k1'].append(i)
    if i<66:
        number['k2'].append(i)
print(number)

"""有如下两个集合，pythons是报名python课程的学员名字集合，ais是报名人工智能课程的学员名字集合
　　pythons={'albert','孙悟空','周星驰','朱茵','林志玲'}
　　ais={'猪八戒','郭德纲','林忆莲'，'周星驰'}
　　1. 求出即报名python又报名ai课程的学员名字集合
　　2. 求出所有报名的学生名字集合
　　3. 求出只报名python课程的学员名字
　　4. 求出没有同时这两门课程的学员名字集合
"""
pythons={'albert','孙悟空','周星驰','朱茵','林志玲'}
ais={'猪八戒','郭德纲','林忆莲','周星驰'}
print(pythons & ais)
print(pythons | ais)
print(pythons - ais)
print(pythons ^ ais)



#去重,无需保持原来的顺序
l=['a','b',1,'a','a']
print(set(l))

#去重,并保持原来的顺序

l1=[1,'a','b',1,'a']
l1=[]
s=set()
for i in l:
    if i not in s:
        s.add(i)
        l1.append(i)

print(l1)



#列表中元素为可变类型时,去重,并且保持原来顺序
l=[
    {'name':'albert','age':18,'sex':'male'},
    {'name':'alex','age':73,'sex':'male'},
    {'name':'alex','age':20,'sex':'female'},
    {'name':'albert','age':18,'sex':'male'},
    {'name':'albert','age':18,'sex':'male'},
]

s=set()
l1=[]
for item in l:
    val=(item['name'],item['age'],item['sex'])
    if val not in s:
        s.add(val)
        l1.append(item)

print(l1)


