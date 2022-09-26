
def check(n):
    for i in range(0, len(n)- 2, 2): 
        if n[i] != n[i+2]: return False
    return True
def solve():
    n = input()
    if check(n) and (n[0] != n[1] ) and len(n)%2 == 1:
        print('YES')
    else: print('NO')
for t in range( int(input())): solve()