def tichchuso(n: int):
    tich = 1
    for i in str(n):
        tich*= int(i)
    return tich
def cmp(tmp):
    return (tmp[1], tmp[0] )
def solve():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = []
    for i in a:
        b.append( (i, tichchuso(i)) )
    b.sort(key = cmp)
    for i in b:
        print(i[0], end = ' ')
    print()
for t in range( int(input())): solve()