n = int(input())
l = {}
for i in range(1, n+1):
    l[i] = []
for i in range(n-1):
    u, v = map(int, input().split())
    l[u].append(v)
    l[v].append(u)
fl = True
for u in range(1, n+1):
    if len(l[u]) == n - 1:
        fl = False
        print("Yes")
        break
if fl:
    print("No")
