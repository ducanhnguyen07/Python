def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(i) for i in input().split()]

res = 0
for i in a:
    cntU = 0
    cntD = 0
    m = i
    while not(checkPrime(m)):
        cntU += 1
        m += 1
    m = i
    while not(checkPrime(m)):
        cntD += 1
        m -= 1
    res = max(min(cntU, cntD), res)
print(res)