a = []
b = []
n = 0
k = 0

def outp():
    for i in range(1, k+1):
        print(b[a[i]-1], end = ' ')
    print()

def Try(i):
    for j in range(a[i-1]+1, n-k+i+1):
        a[i] = j
        if i == k:
            outp()
        else:
            Try(i+1)

n, k = map(int, input().split())
b = [str(i) for i in input().split()]
b = set(b)
b = sorted(b)
for i in range(0, k+1):
    a.append(0)
n = len(b)
Try(1)