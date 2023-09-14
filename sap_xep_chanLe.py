n = int(input())
a = []
while True:
    x = [int(i) for i in input().split()]
    a += x
    if len(a) == n:
        break

odd = []
even = []
for i in a:
    if i % 2:
        odd.append(i)
    else:
        even.append(i)
odd.sort(reverse=True)
even.sort()
io = 0
ie = 0
for i in range(n):
    if a[i] % 2:
        print(odd[io], end = ' ')
        if io < len(odd) - 1:
            io += 1
    else:
        print(even[ie], end = ' ')
        if ie < len(even) - 1:
            ie += 1