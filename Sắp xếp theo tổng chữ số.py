def take_second(tmp):
    return (tmp[1], tmp[0])
def tongchuso(n: str):
    a = [int(i) for i in n ]
    tong = sum(a)
    return tong
def solve():
    n = int(input())
    a = [ int(i) for i in input().split()]
    res = []
    for i in a:
        tmp = (i, tongchuso(str(i)))
        res.append(  tmp)
    
    res = sorted(res, key = take_second )
    for i in res:
        print(i[0] , end = ' ' )
    print()
for t in range( int(input())): solve()