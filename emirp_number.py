import sys

def check(s):
    t = ''.join(reversed(s))
    if t == s:
        return False
    return True

mxn = 10**6+1
p = [True] * mxn
p[0] = p[1] = False
for i in range(2, 1001):
    if p[i]:
        for j in range(i*i, mxn, i):
            p[j] = False

for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        s = str(i)
        s = ''.join(reversed(s))
        if p[i]:
            if check(s) and int(s) < n and p[int(s)] and i < int(s):
                print(i, s, sep = ' ', end = ' ')
                
    print()  
