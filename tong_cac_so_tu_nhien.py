n = 0
a = []
b = []

def outp(n):
    s = "("
    for i in range(1, n+1):
        if i <= n and i > 1:
            s += " "
        s += str(a[i])
    s += ")"
    b.append(s)

def Try(i, k, curSum):
    for j in range(k, 0, -1):
        if curSum + j <= n:
            curSum += j
            a[i] = j
            if curSum == n:
                outp(i)
            else:
                Try(i+1, j, curSum)
            curSum -= j

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(n+1):
        a.append(0)
    b.clear()
    Try(1, n, 0)
    print(len(b))
    for i in b:
        print(i, end = ' ')
    print()

