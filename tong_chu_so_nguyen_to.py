import math

def check(s):
    sum = 0
    for i in s:
        sum = sum + int(i)
    if sum < 2:
        return False
    for i in range(2, int(sum**0.5)+1):
        if sum % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
