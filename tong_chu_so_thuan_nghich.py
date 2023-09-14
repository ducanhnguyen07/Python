import math

def check(s):
    sum = 0
    for i in s:
        sum = sum + int(i)
    s1 = str(sum)
    if len(s1) < 2:
        return False
    s2 = ''.join(reversed(s1))
    if s1 != s2:
        return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
