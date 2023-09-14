def check(s):
    s1 = s
    s2 = s[: :-1]
    for i in range(0, len(s)-1, 1):
        if abs(ord(s1[i+1]) - ord(s1[i])) != abs(ord(s2[i+1]) - ord(s2[i])):
            return False
    return True

t = int(input())
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
