while True:
    a = [int(i) for i in input().split()]
    if a[0] == a[1] == a[2] == a[3] == 0: break
    dem = 0
    while True:
        if a[0] == a[1] == a[2] == a[3] : break
        x = a[0]
        a[0] = abs(a[0]  - a[1])        
        a[1] = abs(a[1]  - a[2])
        a[2] = abs(a[2]  - a[3])
        a[3] = abs(a[3] - x)        
        dem+=1
    print(dem)