n = int(input())
a = []
for i in range(n):
    a.append(list(map(str, input().split())))
idx = 0
res = []
while(idx < n):
    if len(a[idx]) == 6:
        while len(a[idx]) == 6 and idx + 2 <= n:
            idx += 2
            if idx >= n - 1:
                break
        res.append(1)
    else:
        idx += 4
        res.append(2)
    if idx == n-1:
        break
print(len(res))
for i in res:
    print(i)