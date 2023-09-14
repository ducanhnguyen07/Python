def checkPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 0
    return 1
n, m = map(int, input().split())
a = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(n):
    for j in range(m):
        a[i][j] = checkPrime(a[i][j])
for i in range(n):
    for j in range(m):
        print(a[i][j], end = ' ')
    print()