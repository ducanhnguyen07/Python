import math

n, k = map(int, input().split())
st = pow(10, k-1)
fi = pow(10, k) - 1
cnt = 0
for i in range(st, fi+1, 1):
    if math.gcd(i, n) == 1:
        if cnt == 10:
            cnt = 1
            print()
        else:
            cnt += 1
        print(i, end =' ')