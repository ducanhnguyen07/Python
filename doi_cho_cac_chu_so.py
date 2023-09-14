def check(s):
    k = -1
    a = [int(i) for i in s]
    for i in range(len(a)-1, 0, -1):
        if a[i] < a[i-1]:
            k = i-1
            break
    if k == -1:
        print(k)
        return
    idx = -1
    maxx = -1
    for i in range(k+1, len(a)):
        if maxx < a[i] and a[i] < a[k]:
            idx = i
            maxx = a[i]
    if maxx == 0 and k == 0:
        print(-1)
        return
    a[k], a[idx] = a[idx], a[k]
    for i in a:
        print(i, end = "")
    print()
    
for _ in range(int(input())):
    s = input()
    check(s)


# 3512 
# 3215