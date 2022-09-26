def solve():
    n = int(input())
    k = 1000
    while (n%7 != 0):
        n2 =  ''.join( list(reversed(str(n))) )
        n2 = int(n2)
        n = n + n2
        if k == 0: 
            n = -1
            break
        k-=1
    print(n)
for t in range( int(input())): solve()