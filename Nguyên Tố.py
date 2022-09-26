import math
def nguyento(n):
    if n == 0 or n == 1: return 0
    for i in range(2,int(n**0.5) +1):
        if n%i == 0: return 0
    return 1
def solve():
    n = int(input())
    dem = 0
    for i in range(1,n):
        if math.gcd(i,n) == 1: dem+=1
    if nguyento(dem): print('YES')
    else: print('NO')
for t in range( int(input()) ): solve() 