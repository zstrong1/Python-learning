#1、将names=['albert','james','kobe','kd']中的名字全部变大写

names = ['albert','james','kobe','kd']
names = [name.upper() for name in names]

print(names)

#2、将names=['albert','jr_shenjing','kobe','kd']中以shenjing结尾的名字过滤掉，然后保存剩下的名字长度
names=['albert','jr_shenjing','kobe','kd']
names=[len(name) for name in names if not name.endswith('shenjing')]
print(names)

#3、求文件a.txt中最长的行的长度（长度按字符个数算，需要使用max函数）

with open('a.txt','r',encoding='utf-8') as f:
    max_line = max([len(line) for line in f])
    print(max_line)

#4、求文件a.txt中总共包含的字符个数？思考为何在第一次之后的n次sum求和得到的结果为0？（需要使用sum函数）

with open('a.txt','r',encoding='utf-8') as f:
    sum_line = sum([len(line) for line in f])
    print(sum_line)
    print(sum_line)

#5、思考题
with open('a.txt') as f:
    g=(len(line) for line in f)
    print(sum(g))
#文件关闭前操作

# 6、文件shopping.txt内容如下
# mac,20000,3
# lenovo,3000,10
# tesla,1000000,10
# chicken,200,1
# （1）求总共花了多少钱？
#
# （2）打印出所有商品的信息，格式为[{'name':'xxx','price':333,'count':3},...]
#
# （3）求单价大于10000的商品信息,格式同上
with open('a.txt',encoding='utf-8') as f:
    line = f.read().split('\n')
    lines = [k.split(',') for k in line]
    sum_money = sum([ int(k[1])*int(k[2]) for k in lines])
    info =[
        {'name':m[0],
        'price':int(m[1]),
         'count':int(m[2])}
        for m in lines ]
    info_1 =[{'name':m[0],
        'price':int(m[1]),
         'count':int(m[2])}
        for m in lines if int(m[1])>10000]
    print(sum_money)
    print(info)
    print(info_1)