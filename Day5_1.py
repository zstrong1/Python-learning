import os
with open('a.txt') as read_f,open('.a.txt.swap','w') as wirte_f:
    data = read_f.read()
    data1 = data.split('\n')
    data2 = []
    Sum = 0
    for item in data1:
        data2.append(item.split())
    for i in range(3):
        Sum += int(data2[i][1]) * int(data2[i][2])
    print('Sum is:%d'%Sum)
