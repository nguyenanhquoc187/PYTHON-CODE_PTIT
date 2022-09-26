def nguyento(n):
    if n == 0 or n == 1: return 0
    for i in range(2,int(n**0.5) +1):
        if n%i == 0: return False
    return True
def check(n: str):
    for i in list(map(int,n)):
        if not nguyento(i): return False
    return True
def solve():
    n = input()
    n2 =int ( ''.join(list(reversed(n))) )
    tong = sum( [ int(i) for i in n] )
    if nguyento(int(n) ) and nguyento(n2) and nguyento(tong) and check(n):
        print('Yes')
    else: print('No')
for t in range( int(input())): solve()
