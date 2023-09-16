import sys

def rotateLeft(s):
    return s[1:] + s[0]

a = []

n = int(input())
for _ in range(n):
    a.append(input())
res = sys.maxsize
fl = False
for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j:
            s = a[j]
            cntRol = 0
            while s != a[i] and cntRol < len(a[i]):
                s = rotateLeft(s)
                cntRol += 1
            if s != a[i]:
                fl = True
                break
            cnt += cntRol
    res = min(cnt, res)
    if fl:
        break
print(-1) if fl else print(res) 
