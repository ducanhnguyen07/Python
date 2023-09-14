def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(i) for i in input().split()]
p = []
for i in a:
    if checkPrime(i):
        p.append(i)
p.sort()
ip = 0
for i in a:
    if checkPrime(i):
        print(p[ip], end = ' ')
        if ip < len(p) - 1:
            ip += 1
    else:
        print(i, end = ' ')

