n, k = input().split()
n = int(n)
k = int(k)
a = []
b = []

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

for i in range(n+1):
    a.append(0)
c = [int(i) for i in input().split()]
s = set(c)
b = [*s]
b.sort()
n = len(b)

Try(1)



