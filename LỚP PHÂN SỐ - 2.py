from math import gcd
class PhanSo:
    def __init__(self,tu, mau) -> None:
        self.tu = tu
        self.mau = mau

    def TongPhanSo (self, o):
        tu = self.tu*o.mau + self.mau*o.tu
        mau = self.mau * o.mau
        return PhanSo(tu, mau)

    def ToiGian (self):
        tu = self.tu//gcd(self.tu, self.mau)
        mau = self.mau//gcd(self.tu, self.mau)
        return "{}/{}".format(tu, mau)

a = [int(i) for i in input().split()]
p1 = PhanSo(a[0], a[1])
p2 = PhanSo(a[2], a[3])
print(p1.TongPhanSo(p2).ToiGian())