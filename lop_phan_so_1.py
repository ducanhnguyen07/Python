from math import *

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def rutGon(self):
        uc = gcd(self.tu, self.mau)
        self.tu /= uc
        self.mau /= uc

    def __str__(self):
        return f"{self.tu:.0f}/{self.mau:.0f}"
if __name__ == '__main__':
    tu, mau = map(int, input().split())
    p = PhanSo(tu, mau)
    p.rutGon()
    print(p)