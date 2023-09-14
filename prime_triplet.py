import sys

mxn = 10**6+1
prime = [True] * mxn
prime[0] = prime[1] = False
for i in range(2, 1001):
    if prime[i]:
        for j in range(i*i, mxn, i):
            prime[j] = False
a = [i for i in range(mxn) if prime[i]]


for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in a:
        if i + 6 >= n:
            break
        if (prime[i+2] or prime[i+4]) and prime[i+6]:
            cnt += 1
    print(cnt)