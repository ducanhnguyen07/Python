import sys
from math import gcd

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    dp = {0 : 0}
    l = [0]
    for i in range(n):
        for j in l:
            min_dis = gcd(j, a[i])
            fee = dp[j] + c[i]
            if min_dis not in dp:
                dp[min_dis] = fee
                l.append(min_dis)
            else:
                dp[min_dis] = min(fee, dp[min_dis])

    print(dp[1]) if 1 in dp else print(-1)
