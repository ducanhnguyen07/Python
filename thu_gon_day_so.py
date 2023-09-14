n = int(input())
a = []
a = [int(i) for i in input().split()]
b = []
for i in range(0, len(a)):
    if len(b) == 0:
        b.append(a[i])
    elif (b[len(b)-1] + a[i]) % 2 == 0:
        b.pop()
    else:
        b.append(a[i])
print(len(b))