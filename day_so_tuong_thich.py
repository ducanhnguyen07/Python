import sys

n = int(sys.stdin.readline())
a = [int(i) for i in input().split()]
lm = min(a)
res = sys.maxsize
for i in range(1, lm+1):
    fl = 0
    sum = 0
    for j in range(n):
        if a[j]//i == a[j]//(i+1):
            fl = 1
            break
    if fl == 0:
        for j in range(n):
            sum += (a[j]//(i+1) + 1)
        res = min(sum, res)
print(res)
    
