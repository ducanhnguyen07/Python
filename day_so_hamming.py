from queue import Queue
import bisect as bs
import sys

mxn = 10**18

a = Queue()
a.put(1)
hammingNum = []
st = [2, 3, 5]
fl = {1 : 1}

while not(a.empty()):
    top = a.get()
    hammingNum.append(top)
    for i in st:
        if top*i <= mxn and top*i not in fl:
            fl[top*i] = 1
            a.put(top*i)
hammingNum.sort()

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    res = bs.bisect_left(hammingNum, n)
    print(res + 1) if hammingNum[res] == n else print("Not in sequence")
