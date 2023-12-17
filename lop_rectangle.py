class Rectangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimeter(self):
        return (self.a + self.b) * 2
    
    def area(self):
        return self.a * self.b
    
    def color(self):
        return self.c.title()

# if __name__ == '__main__':
arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if r.a > 0 and r.b > 0:
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")