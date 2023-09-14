def cntN(n):
    lim = int(n**0.5) + 1
    prime = [i for i in range(lim)]
    for i in range(2, lim):
        if prime[i] == i:
            for j in range(i*i, lim, i):
                prime[j] = i
    cnt = 0
    for i in range(2, lim):
        p = prime[i]
        q = prime[i // prime[i]]
        if p*q == i and q != 1 and p != q:
            cnt += 1
        elif prime[i] == i:
            if i**8 <= n:
                cnt += 1
    return cnt

print(cntN(int(input())))