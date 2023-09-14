def check(s):
    cntLw = 0
    cntUp = 0
    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z':
            cntLw = cntLw + 1
        elif s[i] >= 'A' and s[i] <= 'Z':
            cntUp = cntUp + 1
    return cntUp > cntLw    
        

s = input()

if check(s):
    print(s.upper())
else:
    print(s.lower())
