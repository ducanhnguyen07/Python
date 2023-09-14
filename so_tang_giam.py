import math

def check(s):
    if len(s) < 3:
        return False
    i = 0
    while(s[i] < s[i+1] and i < len(s) - 1):
        i += 1
    for j in range(i, len(s)-1, 1):
        if s[j] < s[j+1]:
            return False
    return True    

t = int(input())
for _ in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")


