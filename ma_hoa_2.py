p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    s = input()
    if s == "0":
        break
    a = s.split()
    k = int(a[0])
    t = a[1]
    res = ""
    for i in range(0, len(t)):
        idx = 0
        if t[i] == "_":
            idx = 26
        elif t[i] == ".":
            idx = 27
        else:
            idx = ord(t[i]) - ord('A')
        res += str(p[(idx+k) % 28])
    ans = ''.join(reversed(res))
    print(ans)