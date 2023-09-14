def check(s):
    n = len(s)
    if s[n-1] == '6' and s[n-2] == '8':
        return True
    return False

t = int(input())
for i in range(t):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")