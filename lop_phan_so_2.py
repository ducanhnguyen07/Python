from math import *

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def rutGon(self):
        uc = gcd(self.tu, self.mau)
        self.tu //= uc
        self.mau //= uc

    def __add__(self, o):
        ts = self.tu * o.mau + self.mau * o.tu
        ms = self.mau * o.mau
        return PhanSo(ts, ms)

    def __str__(self):
        return f'{self.tu}/{self.mau}'

if __name__ == '__main__':
    a1, b1, a2, b2 = map(int, input().split())
    p = PhanSo(a1, b1) + PhanSo(a2, b2)
    p.rutGon()
    print(p)