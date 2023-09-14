import array
import sys
from math import sqrt

mxn = 2*(10**6)+1
prime = array.array('i', [0]*mxn)

for i in range(2, int(sqrt(mxn - 1))+1):
    if prime[i] == 0:
        prime[i] = i
        for j in range(i*2, mxn, i):
            prime[j] = i
for i in range(4, mxn):
    if prime[i] == 0:
        prime[i] += i
    else:
        prime[i] += prime[i // prime[i]]

t = int(sys.stdin.readline())
sum = 0
for _ in range(t):
    n = int(sys.stdin.readline())
    sum += prime[n]
print(sum)