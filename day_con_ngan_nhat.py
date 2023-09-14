import sys
from math import gcd

for _ in range(int(input())):
    n, k = map(int, input().split())
    a = []
    while True:
        b = [int(i) for i in input().split()]
        a += b
        if len(a) == n:
            break
    res = sys.maxsize
    for i in range(0, n):
        if a[i] % k == 0:
            tmp = a[i]
            for j in range(i, n):
                tmp = gcd(a[j], tmp)
                if tmp == k:
                    res = min(j - i + 1, res)
                    break
                elif tmp < k:
                    break
    print(res) if res <= n else print(-1)