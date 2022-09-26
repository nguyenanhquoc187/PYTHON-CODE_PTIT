def Run(n,p):
    res = 0
    if n<p:
        return 0
    for i in range(p, n+1, p):
        res += Tach_nt(i,p)
    return res

def Tach_nt(x, p):
    res = 0
    while x%p==0:
        x/=p
        res+=1
    return res

t = int(input())
while t>0:
    n, p = map(int, input().split())
    print(Run(n,p))
    t-=1