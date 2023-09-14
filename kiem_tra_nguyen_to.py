import math

def check(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    sum = 0
    for i in range(len(s)-4, len(s), 1):
        sum = sum*10 + int(s[i]) - int('0')
    if check(sum):
        print("YES")
    else:
        print("NO")   
