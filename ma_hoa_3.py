for _ in range(int(input())):
    s = input()
    idx = len(s)//2
    s1 = s[:idx]
    s2 = s[idx:]
    sum1 = sum2 = 0
    for i in range(idx):
        sum1 += ord(s1[i]) - ord('A')
        sum2 += ord(s2[i]) - ord('A')
    res = ""
    for i in range(idx):
        c1 = ord(s1[i]) - ord('A')
        c1 += sum1
        c1 %= 26
        c2 = ord(s2[i]) - ord('A')
        c2 += sum2
        c2 %= 26
        c1 += c2
        c1 %= 26
        res += chr(c1 + 65)
    print(res)
