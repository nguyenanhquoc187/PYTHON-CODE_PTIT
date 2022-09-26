from decimal import Decimal
from math import *


class Point():
    def __init__(self, x, y ):
        self.x  = x
        self.y = y
    def distance(self, p ) :
        d = sqrt( pow(self.x - p.x,2) + pow(self.y - p.y,2) )
        return round(Decimal(d),4)