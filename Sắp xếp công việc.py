t = int(input())
while t > 0:
    n = int(input())
    a = []
    for i in range(n):
        si,fi = map(int,input().split())
        a.append((si,fi))
    a.sort(key = lambda x: x[1])
    dem = 1
    k = a[0][1]
    b = []
    for i in range(1,n):
        if a[i][0] > k:
            dem+=1
            k = a[i][1]
        else:
            b.append(a[i])
    if len(b) > 0: dem+=1
    k = b[0][1]
    for i in range(1,len(b)):
        if b[i][0] > k:
            dem+=1
            k = b[i][1]
    print(dem)
    t-=1