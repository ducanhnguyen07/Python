def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n = int(input())
a = [int(i) for i in input().split()]

b = {}

for i in a:
    if checkPrime(i):
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
for i in b:
    print(i, b[i], sep = " ")