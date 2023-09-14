def convToMin(s, p, q):
    res = ""
    # p < q
    for i in s:
        if ord(i) - ord('0') == q:
            res += str(p)
        else:
            res += str(i)
    return int(res)

def convToMax(s, p, q):
    res = ""
    # p < q
    for i in s:
        if ord(i) - ord('0') == p:
            res += str(q)
        else:
            res += str(i)
    return int(res)

for _ in range(int(input())):
    p, q = input().split()
    s = input()
    a = s.split()
    s1 = ""
    s2 = ""
    if len(a) == 2:
        s1 = a[0]
        s2 = a[1]
    else:
        s1 = s
        s2 = input()
    p = int(p)
    q = int(q)
    if p > q:
        p, q = q, p
    print(convToMin(s1, p, q)+convToMin(s2, p, q), convToMax(s1, p, q)+convToMax(s2, p, q), sep = ' ')
