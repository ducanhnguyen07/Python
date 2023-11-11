from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

class Triangle:
    def __init__(self, p1:Point, p2:Point, p3:Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    def cal(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if a + b <= c or b + c <= a or a + c <= b:
            return 'INVALID'
        return f'{(a + b + c):.3f}'

if __name__ == '__main__':
    a = []
    n = int(input())
    for _ in range(n):
        a += [float(i) for i in input().split()]
    for i in range(0, 6*n, 6):
        tgl = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
        print(tgl.cal())

