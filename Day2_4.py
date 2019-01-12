max_level=5
for current_level in range(1,max_level+1):
    for i in range(max_level-current_level):
        print(' ',end='')
    for j in range(2*current_level-1):
        print('*',end='')
    print()