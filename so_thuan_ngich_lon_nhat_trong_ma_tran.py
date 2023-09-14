def checkPld(n):
    if n < 10:
        return False
    s = str(n)
    cmp = ''.join(reversed(s))
    return s == cmp

n, m = map(int, input().split())
a = [[ 0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
p = []
for i in range(n):
    for j in range(m):
        if checkPld(a[i][j]):
            p.append(a[i][j])
p.sort()
if len(p) == 0:
    print("NOT FOUND")
else:
    x = p[len(p)-1]
    print(x)
    for i in range(n):
        for j in range(m):
            if x == a[i][j]:
                print(f"Vi tri [{i}][{j}]") 
