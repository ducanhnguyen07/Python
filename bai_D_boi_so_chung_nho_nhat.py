import sys

M = 10**9 + 7
mxn = 10**6 + 1
prime = [True] * mxn
p = []

for i in range(2, mxn):
    if prime[i]:
        p.append(i)
        for j in range(i*i, mxn, i):
            prime[j] = False

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, input().split())
    a -= 1
    st = [0]*len(p)
    fi = [0]*len(p)
    res = 1
    for i in range(len(p)):
        dvd = p[i]
        while a >= dvd or b >= dvd:
            st[i] += (a // dvd)
            fi[i] += (b // dvd)
            dvd *= p[i]
        res = res * (2*(fi[i] - st[i]) + 1) % M
    print(res)
