def solve():
    n = input()
    a = list(map(int,n))
    tong = sum(a)
    return tong%3 == 0
for t in range( int(input()) ):
    if solve() : print("YES")
    else: print("NO")