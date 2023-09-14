import math

def check(s):
    s = s.lower()
    t = s[len(s) - 3:]
    if t == ".py" and len(s) >= 3:
        return True
    return False

s = input()
print("yes") if check(s) else print("no")