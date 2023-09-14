def sumStr(a):
    sa = str(a)
    s1 = 1
    for i in sa:
        s1 *= (ord(i) - ord('0'))
    return s1

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    for i in range(0, n):
        for j in range(i+1, n):
            if sumStr(a[i]) > sumStr(a[j]):
                a[i], a[j] = a[j], a[i]
            elif sumStr(a[i]) == sumStr(a[j]):
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
    for i in a:
        print(i, end = ' ')
    print()