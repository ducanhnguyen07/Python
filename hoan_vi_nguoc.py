n = 0
a = []
f = []



def outp(n):
    for i in range(1, n+1):
        print(a[i], end = '')
    print(' ', end = '')


def Try(i):
    for j in range(n, 0, -1):
        if(f[j] == False):
            f[j] = True
            a[i] = j
            if i == n:
                outp(i)
            else:
                Try(i+1)
            f[j] = False

for _ in range(int(input())):
    n = int(input())
    a = [0]*(n+1)
    f = [False]*(n+1)
    sum = 1
    for i in range(2, n+1):
        sum *= i
    print(sum)
    Try(1)
    print()