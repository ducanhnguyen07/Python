def check(s):
    n = len(s)
    if s[0] == s[n-2] and s[1] == s[n-1]:
        return True
    return False

t = int(input())
for i in range(t):
    s = input()

    if check(s):
        print("YES")
    else:
        print("NO")
