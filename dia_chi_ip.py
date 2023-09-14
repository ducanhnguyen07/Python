def check(s):
    for i in s:
        if i.islower():
            return False
    a = s.split('.')
    if len(a) != 4:
        return False
    for i in a:
        if int(i) < 0 or int(i) > 255:
            return False
    return True

for _ in range(int(input())):
    s = input()
    print("YES") if check(s) else print("NO")