import math

def check(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if(n % i == 0):
            return False
    return True

    
    if sum < 2:
        return False
    for i in range(2, n ** 0.5 + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    Gcd = math.gcd(a, b)
    s = str(Gcd)
    sum = 0
    for i in range(len(s)):
        sum = sum + int(s[i]) - int('0')
    if check(sum):
        print("YES")
    else:
        print("NO")
    

