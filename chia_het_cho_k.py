a, k, n = map(int, input().split())

if a % k == 0:
    st = int(a/k)
else:
    st = int(a/k) + 1

fl = 1
st *= k
while(st <= n):
    if st - a > 0:
        print(st - a, end = ' ')
        fl = 0
    st += k
if fl:
    print(-1)
