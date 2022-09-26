def solve():
    n = input()
    a = set(n)
    if check(n) and len(a) == 2: print("YES")
    else: print('NO')

def check(n: str):
    for i in range(2,len(n)):
        if n[i-2] != n[i]: return False
    return True
for t in range( int(input())): solve()