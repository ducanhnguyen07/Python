import math

t = int(input())
for i in range(t):
    s = input()
    for i in range(len(s)):
        if s[i] >= '1' and s[i] <= '9':
            for j in range(int(s[i]) - int('0')):
                print(s[i-1], end = '')
    print()
