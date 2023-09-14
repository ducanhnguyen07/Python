def checkPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return n > 1

n, m = map(int, input().split())
a = [[ 0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
p = []
for i in range(n):
    for j in range(m):
        if checkPrime(a[i][j]):
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
