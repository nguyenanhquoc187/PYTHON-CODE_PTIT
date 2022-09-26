import math
def daoso(n):  
    n = str(n)
    n = list(n)
    n.reverse()
    n = ''.join(n)
    n = int(n)
    return n
def solve():
    n = int(input())
    n1 = daoso(n) 
    if math.gcd(n,n1) == 1: print('YES')
    else: print('NO')
for t in range(int(input())): solve()