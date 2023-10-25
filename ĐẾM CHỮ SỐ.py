t = int(input())
while t >0 :
    a,b = map(int, input().split())
    d = {0:0 ,1:0 ,2:0 ,3:0 ,4:0 ,5:0 ,6:0 ,7:0 ,8:0 , 9:0}
    for i in range(a,b+1):
        for j in list(str(i)):
            d[int(j)]+= 1
    print(*d.values())
    t-=1