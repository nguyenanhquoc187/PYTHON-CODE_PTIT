n = int(input())
d = {}
for i in range(n):
    ten = input()
    bd = input()
    kt = input()
    luongmua = int(input())
    gio = int(kt[0:2]) - int(bd[0:2])
    phut = int(kt[3:]) - int(bd[3:])
    if phut < 0:
        gio-=1
        phut = phut+60
    thoigian = gio + phut/60
    if d.get(ten) == None:
        d[ten] = luongmua,thoigian
    else:
        d[ten] = d[ten][0] + luongmua, d[ten][1] + thoigian
for i in d.keys():
    d[i] = d[i][0]/ d[i][1], d[i][1]
ma = 1
for i,j in d.items():
    print("T0" + str(ma), i, '{:.2f}'.format(j[0]))
    ma+=1
