for _ in range(int(input())):
    s = input()
    a1 = []
    a2 = []
    idx = 1
    for i in range(len(s)):
        if s[i] == '(':
            a1.append(idx)
            a2.append(idx)
            idx += 1
        if s[i] == ')':
            a1.append(a2[len(a2)-1])
            a2.pop()
    for i in a1:
        print(i, end = ' ')
    print()