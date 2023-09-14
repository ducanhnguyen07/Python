for _ in range(int(input())):
    s = input()
    ss = ""
    sum = 0
    for i in s:
        if i.isalpha():
            ss += str(i)
        else:
            sum += ord(i) - ord('0')
    ss = sorted(ss)
    print(*ss, sep = '', end = '')
    print(sum)