def check(a, b):
    for i in a:
        if i not in b:
            return "NO"
    return "YES"

n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a = set(a)
a = sorted(a)
b = set(b)
b = sorted(b)
print(check(a, b))