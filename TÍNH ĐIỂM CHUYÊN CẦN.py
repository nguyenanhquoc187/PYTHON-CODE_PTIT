n = int(input())
d = {}
for i in range(n):
    msv = input()
    ten = input()
    lop = input()
    d[msv] = (ten, lop)
for i in range(n):
    msv, dDanh = map(str,input().split()) 

    point = 10
    for j in dDanh:
        if j == 'v': point-=2
        if j == 'm': point-=1
    if point <= 0:
        point =0
        d[msv] = d[msv] + (0, 'KDDK')
    else:
        d[msv] = d[msv] + (point,)
for i in d.keys():
    print(i, *d[i])

