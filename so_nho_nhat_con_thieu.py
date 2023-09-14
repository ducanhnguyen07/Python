n = int(input())
a = set([int(i) for i in input().split()])

sum = 0
for i in a:
    sum += i
if sum == n*(n + 1)/2:
    print(n+1)
else:
    for i in range(1, n+1):
        if i not in a:
            print(i)
            break