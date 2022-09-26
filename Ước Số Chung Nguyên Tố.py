import math
def nguyento(n):
    if n == 0 or n == 1: return 0
    for i in range(2,int(n**0.5) +1):
        if n%i == 0: return 0
    return 1
def solve():
    a,b = [ int(i) for i in input().split()]
    sum = 0
    for i in list(str(math.gcd(a,b))):
        sum+= int(i)
    if nguyento(sum): print('YES')
    else: print('NO')
for t in range(int(input()) ): solve()