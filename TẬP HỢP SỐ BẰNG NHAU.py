n,m = map(int,input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a = set(a)
b = set(b)
if a ==b: 
    print('YES')
else: print('NO')