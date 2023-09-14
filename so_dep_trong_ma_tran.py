n, m = map(int, input().split())
a = [[ 0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
p = []
maxx = 0
minn = 10**5
for i in range(n):
    maxx = max(max(a[i]), maxx)
    minn = min(min(a[i]), minn)
for i in range(n):
    for j in range(m):
        if a[i][j] == maxx - minn:
            p.append(a[i][j])
p.sort()
if len(p) == 0:
    print("NOT FOUND")
else:
    x = p[0]
    print(x)
    for i in range(n):
        for j in range(m):
            if x == a[i][j]:
                print(f"Vi tri [{i}][{j}]") 
