import sys

for _ in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append((y, x))
    a.sort()
    cnt = 1
    minn = a[0][0]
    for i in range(1, n):
        if minn <= a[i][1]:
            cnt += 1
            minn = a[i][0]
    print(cnt)
    