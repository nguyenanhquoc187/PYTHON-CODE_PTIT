n = int(input())
a= []
for i in range(n):
    b = [int(i) for i in input().split()]
    a.append(b)
k = int(input())
tongNuaDuoi = 0
for i in range(n):
    for j in range(i):
        tongNuaDuoi += a[i][j]
tongNuaTren = 0
for i in range(n):
    for j in range(i+1,n):
        tongNuaTren += a[i][j]
doChechLech = abs( tongNuaTren - tongNuaDuoi)
if doChechLech <= k: print('YES')
else: print('NO')
print(doChechLech)
