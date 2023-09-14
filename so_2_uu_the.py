from queue import Queue

def check(s):
    cnt = s.count('2')
    if cnt*2 > len(s) and s[0] != "0":
        return True
    return False

a = []
Q = Queue()
Q.put("0")
Q.put("1")
Q.put("2")
while True:
    top = Q.get()
    if check(top):
        a.append(top)
        if len(a) == 1000:
            break
    Q.put(top + "0")
    Q.put(top + "1")
    Q.put(top + "2")
for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        print(a[i], end = ' ')
    print()
