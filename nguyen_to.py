import math

def check(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if(n % i == 0):
            return False
    return True

t = int(input())

for i in range(t):
    a = int(input())
    k = 0
    for i in range(a):
        if math.gcd(i, a) == 1:
            k = k + 1
    if check(k):
        print("YES")
    else:
        print("NO")
    
    
    