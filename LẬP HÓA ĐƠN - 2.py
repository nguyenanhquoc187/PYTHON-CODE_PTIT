from datetime import datetime
class KhachHang:
    sma = 1
    def __init__(self,ten,sophong,ngayden, ngaydi, tiendv) -> None:
        self.ma = 'KH{:02d}'.format(self.sma)
        self.ten = ten.strip()
        self.sophong = sophong.strip()
        self.ngayden = ngayden.strip()
        self.ngaydi = ngaydi.strip()
        self.tiendv = int(tiendv.strip())
        KhachHang.sma +=1
    def getNgayO(self):
        vao = datetime.strptime(self.ngayden, '%d/%m/%Y')
        ra = datetime.strptime(self.ngaydi, '%d/%m/%Y')
        return (ra- vao).days+1
    def getThanhTien(self):
        tang = int(self.sophong[0])
        if tang == 1:
            return 25*self.getNgayO() + self.tiendv
        if tang == 2:
            return 34*self.getNgayO() + self.tiendv
        if tang == 3:
            return 50*self.getNgayO() + self.tiendv
        return 80*self.getNgayO() + self.tiendv
    def __str__(self) -> str:
        return '{} {} {} {} {}'.format(self.ma, self.ten, self.sophong,self.getNgayO(),self.getThanhTien())

if __name__ =='__main__':
    n = int(input())
    a= []
    for i in range(n):
        a.append(KhachHang(
            ten = input(),
            sophong = input(),
            ngayden= input(),
            ngaydi= input(),
            tiendv= input()
        ))
    a.sort(key = lambda x: -x.getThanhTien())
    for i in a:
        print(i)
