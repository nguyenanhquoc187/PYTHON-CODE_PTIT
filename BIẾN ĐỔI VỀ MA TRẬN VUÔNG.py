n, m = map(int, input().split())
a = [[0] for i in range(n+1) ]
for i in range(1, n+1):
    x = [int(i) for i in input().split()]
    a[i].extend(x)

if n > m:
    sohangcanxoa = n - m
    hangxoa = []
    j = 1
    while sohangcanxoa > 0:
        hangxoa.append(j)
        j+=2
        sohangcanxoa-=1
    for i in reversed(hangxoa):
        a.pop(i)
else:
    socotcanxoa = m - n
    cotxoa = []
    j = 2
    while socotcanxoa > 0:
        cotxoa.append(j)
        j+=2
        socotcanxoa-=1
    for i in reversed(cotxoa):
        for j in range(1,n+1):
            a[j].pop(i)
for i in range(1, min(n,m) +1):
    print(*a[i][1:min(n,m)+1])
