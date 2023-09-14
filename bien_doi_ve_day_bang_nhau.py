import sys

n = int(input())
a = [int(i) for i in input().split()]

cnt = 0
res = sys.maxsize
el = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        cnt += abs(a[i] - a[j])
    if cnt < res:
        res = cnt
        el = a[i]
print(res, el, sep = ' ')
    