import math

def check(s):
    t = ''.join(reversed(s))
    for i in range(0, len(s) - 1):
        if abs(ord(s[i]) - ord(s[i+1])) != abs(ord(t[i]) - ord(t[i+1])):
            return False
    return True

for _ in range(int(input())):
    s = input()
    print("YES") if check(s) else print("NO")