n = int(input())
a = [int(i) for i in input().split()]
a.sort()
mul = []
mul.append(a[0]*a[1]*a[2])
mul.append(a[n-1]*a[n-2]*a[n-3])
mul.append(a[0]*a[1])
mul.append(a[n-1]*a[n-2])
mul.append(a[0]*a[1]*a[n-1])
mul.append(a[0]*a[n-1]*a[n-2])
print(max(mul))