from datetime import *

class CaThi:
    j = 1
    def __init__(self, ngaythi, giothi, phongthi):
        self.ma = 'C' + '{:03d}'.format(CaThi.j)
        CaThi.j+=1
        self.ngaygiothi = datetime.strptime( ngaythi + ' ' + giothi , '%d/%m/%Y %H:%M')  
        self.phongthi = phongthi
    def getNgaythi(self):
        return self.ngaygiothi.strftime("%d/%m/%Y")
    def getGioThi(self):
        return self.ngaygiothi.strftime("%H:%M")
    def __str__(self):
        return self.getNgaythi() + ' ' + self.getGioThi() + ' ' + self.phongthi
class Monhoc:

    def __init__(self, ma ,ten, hinhthucthi):
        self.ma = ma
        self.ten = ten
        self.hinhthucthi = hinhthucthi
class Lichthi:
    def __init__(self,macathi, mamon,manhom,soSv):
        self.mamon = mamon
        self.macathi = macathi
        self.manhom = manhom
        self.soSv = soSv
    def __str__(self):
        return self.mamon + ' ' + self.macathi + ' ' + self.manhom + ' ' + self.soSv

def cmp(tmp):
    global listCathi
    global listMonthi
    x = ''
    for i in listCathi:
        if tmp.macathi == i.ma:
            x = i.ngaygiothi
            break
    return (x,tmp.macathi)

if __name__ == '__main__':
    with open('MONTHI.in') as file:
        monthi = file.read().split('\n')
    with open('CATHI.in') as file:
        cathi = file.read().split('\n')
    with open('LICHTHI.in') as file:
        lichthi = file.read().split('\n')
    n_monthi = int(monthi[0])
    n_cathi = int(cathi[0])
    n_lichthi = int(lichthi[0])
    listMonthi = []
    listCathi = []
    listLichthi = []
    for i in range(1,3*n_monthi+1,3):
        listMonthi.append( Monhoc(monthi[i],monthi[i+1],monthi[i+2]) )
    for i in range(1,3*n_cathi+1,3):
        listCathi.append( CaThi(cathi[i],cathi[i+1],cathi[i+2]) )
    for i in range(1,n_lichthi+1):
        a = lichthi[i].split()
        listLichthi.append(Lichthi(a[0],a[1],a[2],a[3]))
    listLichthi.sort(key= cmp)
    for i in listLichthi:
        for j in listCathi:
            if i.macathi == j.ma:
                print(j, end = ' ')
        for j in listMonthi:
            if str(i.mamon) == str(j.ma):
                print(j.ten, end = ' ')
        print(i.manhom + ' ' + i.soSv)
    