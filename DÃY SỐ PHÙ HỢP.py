def DaySo_PhuHop(n,a,b):
    for i in range(0,n):
        if a[i]>b[i]:
            return 0
    return 1

def Check (n,a,b):
    if DaySo_PhuHop(n,a,b):
        print("YES")
    else:
        print("NO")
t = int (input())

while t>0:
    n = int (input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    Check(n,a,b)
    t-=1