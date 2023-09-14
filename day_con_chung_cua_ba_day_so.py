for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    res = []
    i = j = l = 0
    while i<n and j<m and l<k:
        if a[i] == b[j] == c[l]:
            res.append(a[i])
            i += 1
            j += 1
            l += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[l]:
            j += 1
        else:
            l += 1
    if len(res) == 0:
        print("NO", end = '')
    for i in res:
        print(i, end = ' ')
    print()
            
        
