import math

def check(s):
    for i in range(len(s)):
        if s[i] != '1' and s[i] != '0' and s[i] != '2':
            return False
    return True  

t = int(input())
for _ in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")


