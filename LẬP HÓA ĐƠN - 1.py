class KhachHang():
    def __init__(self, j, ten, csc, csm):
        self.ma ='KH' + '{:02d}'.format(j)
        self.ten = ten
        self.csc = csc
        self.csm = csm
    def getThanhtien(self):
        tieuthu = self.csm - self.csc
        if tieuthu <= 50: 
            return tieuthu*100*1.02
        if tieuthu > 50 and tieuthu <= 100:
            return (50*100 + (tieuthu-50)*150)*1.03
        if tieuthu > 100:
            return (50*100 + 50*150 +(tieuthu-100)*200)*1.05
    def __str__(self):
        return self.ma + ' ' + self.ten + ' ' + str(round(self.getThanhtien()))
a = []
for t in range(int(input())):
    ten = input()
    csc = int(input())
    csm = int(input())
    x = KhachHang(t+1,ten,csc,csm)
    a.append(x)
for i in sorted(a, key = lambda o: -o.getThanhtien() ):
    print(i)

