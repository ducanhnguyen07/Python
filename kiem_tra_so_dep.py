import math

def check(s):
    sc = set()
    for i in range(len(s)):
        sc.add(s[i])
    if len(sc) != 2:
        return False
    for i in range(0, len(s) - 2, 1):
        if s[i] != s[i+2]:
            return False
    return True

t = int(input())
for _ in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
    


