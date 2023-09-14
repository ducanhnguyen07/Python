def check(s):
    t = s.replace("688", "")
    if len(t) == 0:
        return True
    t1 = t.replace("68", "")
    if len(t1) == 0:
        return True
    t2 = t1.replace("6", "")
    if len(t2) == 0:
        return True
    return False

s = input()
print("YES") if check(s) else print("NO")
