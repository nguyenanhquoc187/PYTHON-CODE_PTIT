
import math

def solve():
    n,x,m = [float(i) for i in input().split()]
    n2 = math.log(m/n, (1+ x/100) )
    print(int(n2) + 1)
for t in range(int(input())): solve()
