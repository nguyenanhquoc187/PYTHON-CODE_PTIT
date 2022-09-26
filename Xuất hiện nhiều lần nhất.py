def solve():
    n = int(input() )
    a =  [ int(i) for i in input().split()]
    b = {}
    a.sort()
    for i in a:
        if i in b:
            b[i]+=1
        else: b[i] = 1
    Min = 0
    b[Min] = 0
    for i in b:
        if b.get(i) > b.get(Min):
            Min = i
    if b.get(Min) > n/2: print(Min)
    else: print('NO')
for t in range(int(input())): solve()