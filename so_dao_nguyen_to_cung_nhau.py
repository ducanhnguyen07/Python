import math

def check(n):
    m = n
    sum = 0
    while m >= 1:
        sum = sum*10 + int(m%10)
        m /= 10
    if math.gcd(sum, n) == 1: 
        return True
    return False

t = int(input())
for i in range(t):
    n = int(input())
    if check(n):
        print("YES")
    else:
        print("NO")