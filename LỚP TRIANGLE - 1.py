from decimal import ROUND_HALF_UP, Decimal
from math import *
import sys

class Point():
    def __init__(self, x, y ):
        self.x  = x
        self.y = y
    def getDistance(self, p ) :
        d = sqrt( pow(self.x - p.x,2) + pow(self.y - p.y,2) )
        return d
class Triangle():
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def valid(self):
        d1 = self.p1.getDistance(self.p2)
        d2 = self.p1.getDistance(self.p3)
        d3 = self.p2.getDistance(self.p3)
        return((d1 + d2 > d3) and (d1 + d3 > d2) and (d2 + d3 > d1) )
    def getperimeter(self):
        d1 = self.p1.getDistance(self.p2)
        d2 = self.p1.getDistance(self.p3)
        d3 = self.p2.getDistance(self.p3)
        perimeter = d1 + d2 + d3
        return perimeter

if __name__ == "__main__":
    a = []
    for line in sys.stdin:
        for x in line.split():
            a.append(x)
    t = int(a[0])
    i = 1
    while t > 0:
        x1, y1, x2, y2, x3, y3 = float(a[i]), float(a[i+1]), float(a[i+2]), float(a[i+3]), float(a[i+4]), float(a[i+5])
        tamgiac = Triangle(Point(x1,y1), Point(x2,y2), Point(x3,y3))
        if tamgiac.valid():
            print("{:.3f}".format(tamgiac.getperimeter() ) )
        else:
            print("INVALID")
        t -= 1
        i += 6