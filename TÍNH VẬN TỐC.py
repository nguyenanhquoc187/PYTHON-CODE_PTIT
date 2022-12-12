timeStart = 6
ditance = 120
d = {}
n = int(input())
for i in range(n):
    ten = input()
    donvi = input()
    timeFinish = input()
    tmp = (donvi +' ' + ten).split()
    ma =''
    index = timeFinish.index(':')
    for i in tmp:
        ma = ma+ i[0]
    vantoc = ditance/ (int(timeFinish[0:index]) + int(timeFinish[index+1:4])/60  - timeStart)
    # vantoc = round(vantoc)
    d[ma] = ten,donvi, vantoc
a = [ (i, j[2] ) for i,j in d.items()]
for i in sorted(a, key = lambda k: k[1], reverse= True):
    print(i[0], end= ' ')
    x = d[i[0]]
    print(x[0],x[1], round(x[2]), 'Km/h')
