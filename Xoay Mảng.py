def xoaymang( a: list , d: int ):
    while d >0:
        x = a[0]
        a.pop(0)
        a.append( x )
        d-=1
    return a
        
def solve():
    n, d = [int(i) for i in input().split() ]
    a=[ int(i) for i in input().split()]
    a = xoaymang(a,d)
    print(*a, sep = ' ')
for t in range( int(input()) ) : solve()
    