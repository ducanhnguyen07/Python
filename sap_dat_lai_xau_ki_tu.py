for t in range(int(input())):
    a = input()
    b = input()
    a = sorted(a)
    b = sorted(b)
    print(f"Test {t+1}:", end = ' ')
    print("YES") if a == b else print("NO")