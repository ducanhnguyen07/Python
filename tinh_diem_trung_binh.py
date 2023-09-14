from math import gcd

n = int(input())
a = [float(i) for i in input().split()]
a.sort()
st = 0
while a[st] == a[st+1]:
    st += 1
fi = n-1
while a[fi] == a[fi-1]:
    fi -= 1
sum = 0
for i in range(st+1, fi):
    sum += a[i]
print(format(sum/(fi-st-1), '.2f'))
