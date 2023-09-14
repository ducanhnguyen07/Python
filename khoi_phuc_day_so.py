n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
sumT = sum(sum(i) for i in a) // (2*n - 2)
for i in a:
    print((sum(i) - sumT) // (n-2), end = ' ')