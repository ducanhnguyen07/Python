def cnt(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += ord(i) - ord('0')
    return sum

n = int(input())
d = 0
while abs(n) > 9:
    n = cnt(n)
    d += 1
print(d)