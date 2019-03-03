with open('a.txt','r',encoding='utf-8') as f:
    list1 = (line.split() for line in f)
    info = [{'name':name,'sex':sex,'age':age,'salary':salary} \
            for name,sex,age,salary in list1

    ]
    #print(info)
    # print(max(info,key= lambda x: x['salary']))
    # print(min(info,key= lambda x: x['age']))
    info_new = map(lambda item: {'name': item['name'].capitalize(),'sex': item['sex'],'age': item['age'],'salary': item['salary']},info)
    print(list(info_new))
    g = filter(lambda item: item['name'].startswith('a'), info)
    print(list(g))


    def fib(a, b, stop):
        if a > stop:
            return
        print(a, end=' ')
        fib(b, a + b, stop)


    fib(0, 1, 10)
    l = [1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15]]]]]]]
    def get(seq):
        for item in seq:
            if type(item) is list:
                get(item)
            else:
                print(item)
    get(l)