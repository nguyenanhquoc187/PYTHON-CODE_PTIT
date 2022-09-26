class Rectangle:
    def __init__(self, height, width, Color):
        self.height = height
        self.width = width
        self.Color = Color

    def perimeter(self):
        return (self.height + self.width) *2
    def area (self):
        return self.height * self.width
    def color (self):
        return self.Color.lower().capitalize()

arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if r.height >0 and r.width>0:
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")
