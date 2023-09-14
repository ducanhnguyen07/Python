import sys

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [int(i) for i in input().split()]
    res = []
    maxx = -sys.maxsize
    for i in a:
        maxx = max(i, maxx)
    fl = True
    for i in a:
        if i == maxx and fl:
            res.append(m)
            fl = False
        res.append(i)
    for i in res:
        if i < 0:
            print(i, end = ' ')
    for i in res:
        if i >= 0:
            print(i, end = ' ')
    print()