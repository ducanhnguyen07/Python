import re

def check(s):
    if s == "":
        return False
    for i in s:
        if not(i.isalpha()) and not(i.isdigit()):
            return False
    return True

a = {}
n, k = map(int, input().split())
for _ in range(n):
    b = re.split(r"[ ,.?!:;()-/]", input().lower())
    for i in b:
        if check(i):
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
res = list(a.items())
res.sort(key = lambda x : (-x[1], x[0]))
for i in res:
    if i[1] >= k:
        print(i[0], i[1])
    
