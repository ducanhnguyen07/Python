def checkPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
a = [int(i) for i in input().split()]

b = []
p = []
for i in range(n):
    p.append(0)
for i in a:
    if i not in b:
        b.append(i)
m = len(b)
for i in range(m):
    p.append(0)
p[0] = b[0]
for i in range(1, m):
    p[i] = p[i-1] + b[i]
fl = 1
for i in range(m):
    if (checkPrime(p[i]) and checkPrime(p[m-1] - p[i])) or (len(b) == 1 and checkPrime(p[i])):
        print(i)
        fl = 0
        break
if fl:
    print("NOT FOUND")