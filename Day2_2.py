user_name1 = 'user01'
password1 = 123
user_name2 = 'user02'
password2 = 456
user_name3 = 'user03'
password = 789
i = 2
j = 2
k = 2
while(1):
    print('input user name')
    name = input()
    print('input password')
    password = int(input())
    if name == user_name1:
        if i>0:
            if password == password1:
                print('yes,come in')
                break
            else:
                i -=1
        else:
            print('user locked')
    elif name == user_name2:
        if j>0:
            if password == password2:
                print('yes,come in')
                break
            else:
                j -=1
        else:
            print('user locked')
    elif name == user_name3:
        if k>0:
            if password == password3:
                print('yes,come in')
                break
            else:
                k -=1
        else:
            print('user locked')





