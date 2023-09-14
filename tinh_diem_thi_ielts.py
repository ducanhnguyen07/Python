def conv(n):
    n = int(n)
    if n <= 4:
        return 2.5
    elif n <= 6:
        return 3.0
    elif n <= 9:
        return 3.5
    elif n <= 12:
        return 4.0
    elif n <= 15:
        return 4.5
    elif n <= 19:
        return 5.0
    elif n <= 22:
        return 5.5
    elif n <= 26:
        return 6.0
    elif n <= 29:
        return 6.5
    elif n <= 32:
        return 7.0
    elif n <= 34:
        return 7.5
    elif n <= 36:
        return 8.0
    elif n <= 38:
        return 8.5
    return 9.0       

for _ in range(int(input())):
    n, m, s1, s2 = map(float, input().split())
    sc = (conv(n) + conv(m) + s1 + s2)/4.0

    if sc - int(sc) < 0.25:
        print(float(int(sc)))
    elif sc - int(sc) <= 0.5 or (sc - int(sc) > 0.5 and sc - int(sc) < 0.75):
        print(float(int(sc)) + 0.5)
    else:
        print(float(int(sc)) + 1.0)