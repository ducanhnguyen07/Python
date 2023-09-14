import re

def check(s):
    if s == "":
        return False
    for i in s:
        if not(i.isalpha()):
            return False
    return True

a = {}
for _ in range(int(input())):
    b = re.split(r"[ ,.?!:;()-/\d]+", input().lower())
    for i in b:
        if check(i):
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
res = list(a.items())
res.sort(key = lambda x : (-x[1], x[0]))
for i in res:
    print(i[0], i[1])