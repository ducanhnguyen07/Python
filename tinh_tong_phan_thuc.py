import math

t = int(input())
for _ in range(t):
    n = int(input())
    sum = 0
    if n % 2:
        for i in range(1, n+2, 2):
            sum += float(1)/float(i)
    else :
        for i in range(2, n+2, 2):
            sum += float(1)/float(i)
    print(f"{sum :.6f}")