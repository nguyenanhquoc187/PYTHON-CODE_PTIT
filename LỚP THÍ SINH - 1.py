from multiprocessing import set_forkserver_preload


class ThiSinh:
    def __init__(self, ten, ngaysinh, point1, point2, point3):
        self.ten = ten
        self.ngaysinh = ngaysinh
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
    def display(self):
        print('{} {} {:.1f}'.format(self.ten,self.ngaysinh, self.point1 + self.point2 + self.point3) )

a = ThiSinh(input(), input(), float(input()), float(input()), float(input()) )
a.display()
    