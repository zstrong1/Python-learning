# 1、写函数，，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
def filewriter(filename,comment):
        with open(filename,'w') as f:
            f.write(comment)
filewriter('a.txt','fuck')
# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数
def calculate(string):
    i = 0
    j = 0
    k = 0
    m = 0
    for key in string:
        if ord(key) >= 65 and ord(key) <= 122:
            j += 1
        elif ord(key) >= 48 and ord(key) <= 57:
            i += 1
        elif ord(key) == 32:
            k += 1
        else:
            m += 1
    print('【数字】：{}，【字母】：{}，【空格】：{}，【其他】：{}'.format(i,j,k,m))
calculate('shfgdh   123')

# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def lengh(a):
    if len(a) > 5:
        print('长度大于5')
    else:
        print('长度小于5')
lengh('heubuwin')
lengh([12,23,23])
# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def newlist(list1):
    list2 = []
    for i in range(len(list1)):
        if i == 2:break
        list2.append(list1[i])
    return list2
print(newlist([12,34,54]))
print(newlist([23]))

# 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
def oo(b):
    list2 = []
    i = 0
    while(i < len(b)):
        list2.append(b[i])
        i = i+2
    return list2
print(oo([34,35,23,67,43]))
print(oo((12,34,56,76,54)))

# 6、写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。

dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# PS:字典中的value只能是字符串或列表

def newdict(dict):
    for key in dict:
        dict[key] = newlist(dict[key])
    return dict
print(newdict(dic))