from math import gcd

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    l = a[0]
    r = a[n-1]
    cnt = 0
    for i in range(l, r + 1):
        if i not in a:
            cnt += 1
    print(cnt)




