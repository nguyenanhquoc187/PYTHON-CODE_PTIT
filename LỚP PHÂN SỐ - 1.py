from math import gcd


class PhanSo():
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        ucln = gcd(self.mau, self.tu)
        self.tu//= ucln
        self.mau//= ucln
a,b = map(int,input().split())
p = PhanSo(a,b)
p.rutgon()
print(p.tu, '/', p.mau, sep ='')