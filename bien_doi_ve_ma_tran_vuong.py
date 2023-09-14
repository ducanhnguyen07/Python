n, m = map(int, input().split())
a = [[ 0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
if n > m:
    cnt = 0
    for i in range(n):
        if cnt < n - m:
            if i % 2 != 0:
                print(*a[i])
            else:
                cnt += 1     
        else:
            print(*a[i])
else:
    b = []
    res = []
    cnt = 0
    for col in zip(*a):
        b.append(col)
    for i in range(m):
        if cnt < m - n:
            if i % 2 == 0:
                res.append(b[i])
            else:
                cnt += 1     
        else:
            res.append(b[i])
    for col in zip(*res):
        print(*col)
        