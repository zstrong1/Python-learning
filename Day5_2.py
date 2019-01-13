import os

with open('a.txt') as read_f,open('.a.txt.swap','w') as write_f:
    for line in read_f:
        line=line.replace('mac','Linux')
        write_f.write(line)

os.remove('a.txt')
os.rename('.a.txt.swap','a.txt')