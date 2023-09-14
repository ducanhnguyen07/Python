import math

t = int(input())
for i in range(t):
    s = input()
    cnt = 1
    for i in range(len(s)):
        if i == len(s) - 1:
            if s[i] == s[i-1]:
                print(cnt, s[i], sep = "", end = '')
            else:
                print(1, s[i], sep = "", end = '')
        elif s[i] != s[i+1]:
            print(cnt, s[i], sep = "", end ='')
            cnt = 1
        else:
            cnt += 1
    print()
