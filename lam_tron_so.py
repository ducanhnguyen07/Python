import math

t = int(input())

for i in range(t):
    a = int(input())
    fl = 0
    res = 1
    while(a/10 >= 1):
        tmp = a % 10
        res = res * 10
        if tmp >= 5 or (fl == 1 and tmp + 1 >= 5):
            fl = 1
        else:
            fl = 0
        a = a/10
    if fl == 1:
        res = (int(a) + 1) * res
    else :
        res = int(a) * res
    print(res)
    
    