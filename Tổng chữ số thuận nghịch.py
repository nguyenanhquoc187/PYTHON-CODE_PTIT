def tongchuso(n: str):
    a = [int(i) for i in n ]
    tong = sum(a)
    return tong
def ktThuannghich(n: str):
    a = list(n)
    b = a.copy()
    b.reverse()
    return (a == b)
def solve():
    n = input()
    if ktThuannghich(  str(tongchuso(n)) ) and  tongchuso(n) > 9:
        print("YES")
    else: print("NO")
for t in range( int(input()) ):  solve() 