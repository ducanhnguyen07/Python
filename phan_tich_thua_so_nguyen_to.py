import math

t = int(input())
for i in range(t):
    n = int(input())
    print("1 * ", end = "")
    for i in range(2, int(n**0.5)+1, 1):
        cnt = 0
        while(n % i == 0):
            cnt += 1
            n /= i
        if(cnt) :
            print(i, "^", cnt, sep = "", end = '')
            if(n > 1):
                print(" *", end = ' ')
    if(n > 1):
        print(int(n), "^1", sep = "", end = '')
    print()
