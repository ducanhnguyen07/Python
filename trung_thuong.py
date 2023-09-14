for _ in range(int(input())):
    n = int(input())
    a = []
    b = []
    for i in range(n):
        x = int(input())
        a.append(x)
    for i in range(1005):
        b.append(0)
    a.sort()
    for i in a:
        b[i] += 1
    ma = 0
    for i in a:
        ma = max(b[i], ma)
    for i in a:
        if ma == b[i]:
            print(i)
            break