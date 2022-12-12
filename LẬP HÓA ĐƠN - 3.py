n = int(input())
d = {}
for i in range(n):
    maMh = input()
    ten = input()
    soluong = int(input())
    dongia = int(input())
    chietkhau = int(input())
    d[maMh] = ten,soluong,dongia,chietkhau, dongia*soluong - chietkhau

a = [ (i, j[4]) for i,j in d.items() ]
for i in sorted(a, key = lambda k: k[1], reverse= True):
    print(i[0], *d[i[0]])
    
