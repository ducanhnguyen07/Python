n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
k = int(input())
sU = 0
sL = 0
for i in range(n):
    for j in range(n):
        if j > i:
            sU += a[i][j]
        elif j < i:
            sL += a[i][j]
print("YES") if (abs(sU - sL) <= k) else print("NO")
print(abs(sU - sL)) 