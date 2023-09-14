for _ in range(int(input())):
    b = int(input())
    x = input()
    x = int(x, 2)
    if b == 2:
        print(bin(x)[2:])
    elif b == 8:
        print(oct(x)[2:])
    elif b == 16:
        h = format(x, 'X')
        print(h)
    else:
        a = []
        while x > 0:
            a.append(x % b)
            x //= b
        a.reverse()
        print(*a, sep = "")