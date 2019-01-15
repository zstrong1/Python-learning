"""需求:
    用户名和密码存放于文件中，格式为：Albert|Albert123
    启动程序后，先登录，登录成功则让用户输入工资,然后打印商品列表，失败则重新登录，
    超过三次则退出程序,并将用户名添加到黑名单，再次启动程序登陆改用户名，提示用户禁止登陆
    允许用户根据商品编号购买商品
    用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
    可随时退出，退出时，打印已购买商品和余额"""

with open('UserInformation.txt','r') as read_f:
    data = read_f.read()
    data1 = data.split('\n')
    data2 = []
    for key in data1:
        data2.append(key.split('|'))
    user_data = dict(data2)
with open('BlackList.txt','r') as read_f1:
    blacklist = read_f1.read()
    blacklist = blacklist.split('\n')
goods ={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
i = 3
buyer = []
salary = 0
tag = True
while (i and tag):
    user_name = input('请输入用户名>>:')
    if user_name in user_data.keys() and user_name not in blacklist:
        user_password = input('请输入密码>>:')
        if user_password == user_data[user_name]:
            salary = int(input('请输入工资>>:'))
            while tag:
                print(goods)
                good1 = input('请输入需要的商品>>:')
                if good1 in goods.keys():
                    salary -= goods[good1]
                    buyer.append(good1)
                    if salary <= 0:
                        print('余额不足')
                        tag = False
                        buyer.pop()
                j = input('是否继续购买其他产品>>')
                if j == 'n':
                    print('购买的商品：{},余额:{}'.format(buyer,salary))
                    tag = False
        else:
            i -= 1
            continue
    else:
        print('用户名无效或者被锁定')
if i == 0:
    with open('BlackList.txt', 'a+') as write_f:
        write_f.write('\n'+user_name)
