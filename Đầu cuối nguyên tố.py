def nguyento(n):
    if n == 0 or n == 1: return 0
    for i in range(2,int(n**0.5) +1):
        if n%i == 0: return False
    return True

def solve():
    n = input()
    a = int( n[0] + n[1] + n[2])
    b = int( n[-3] + n[-2] + n[-1] )
    if nguyento(a) and nguyento(b):
        print('YES')
    else: print('NO')

for t in range( int(input())): solve()

