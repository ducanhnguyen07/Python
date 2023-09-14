import math

t = int(input())
for _ in range(t):
    s = input()
    sum = 1
    for i in range(len(s)):
        if s[i] != '0':
            sum = sum * (int(s[i]) - int('0'))
    print(sum) 
