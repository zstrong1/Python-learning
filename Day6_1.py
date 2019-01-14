"""要求：
    打印三级菜单如：省，市，县，可以自由发挥
    可返回上一级
    可随时退出程序
"""
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '电子厂':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
i = 1
while i:
    if i == 1:
        for key in menu:
            print(key)
        choice1 = input("第一层>>:")
        if choice1 == 'b' or choice1 == 'q':
            break
        elif choice1 not in menu:
            continue
        else:
            i += 1
    if i == 2:
        for key in menu[choice1]:
            print(key)
        choice2 = input("第二层>>:")
        if choice2 == 'q':
            break
        elif choice2 == 'b':
            i -= 1
            continue
        elif choice2 not in menu[choice1]:
            continue
        else:
            i += 1
    if i == 3:
        for key in menu[choice1][choice2]:
            print(key)
        choice3 = input("第三层>>:")
        if choice3 == 'q':
            break
        elif choice3 == 'b':
            i -= 1
            continue
        elif choice3 not in menu[choice1][choice2]:
            continue



