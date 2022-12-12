from datetime import *

class Gamer():
    def __init__(self, ma, ten , vao : str ,ra: str):
        self.ma = ma
        self.ten = ten
        self.vao = datetime.strptime(vao, '%H:%M')
        self.ra = datetime.strptime(ra, '%H:%M')
    def getGiochoi(self):
        giochoi = self.ra - self.vao
        return giochoi.total_seconds()
    def __str__(self):
        x = datetime.strptime('0:0','%H:%M')
        giochoi = self.ra - self.vao
        giochoi = x + giochoi
        return self.ma + ' ' + self.ten + ' ' + str(giochoi.hour )+ ' gio ' + str(giochoi.minute) + ' phut'
        
n = int(input())
ds = []
for j in range(n):
    ma = input()
    ten = input()
    vao = input()
    ra = input()
    x = Gamer(ma,ten,vao,ra)
    ds.append(x)
for i in sorted(ds,key= lambda o: -o.getGiochoi()):
    print(i)
