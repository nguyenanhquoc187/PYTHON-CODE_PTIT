def solve():
    s = input()
    s = s[-4] + s[-3] + s[-2] + s[-1]
    n = int(s)
    if nguyento(n): print('YES')
    else: print('NO')

def nguyento(n):
    if n == 0 or n == 1: return 0
    for i in range(2,int(n**0.5) +1):
        if n%i == 0: return False
    return True
for t in range(int(input())): solve()