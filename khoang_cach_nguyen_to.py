def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

a = []
for i in range(10005):
    if checkPrime(i):
        a.append(i)

n, x = map(int, input().split())
print(x, end = ' ')
tmp = x
for i in range(n):
    print(tmp + a[i], end = ' ')
    tmp += a[i]
    