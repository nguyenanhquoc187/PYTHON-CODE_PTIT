n = int(input())
a= []
for i in range(n):
    b = [int(i) for i in input().split()]
    a.append(b)
k = int(input())
tongNuaTren = 0
for i in range(n):
    for j in range(n-i-1):
        tongNuaTren += a[i][j]
tongNuaDuoi = 0
for i in range(n):
    for j in range(n-i,n):
        tongNuaDuoi += a[i][j]
doChechLech = abs( tongNuaTren - tongNuaDuoi)
if doChechLech <= k: print('YES')
else: print('NO')
print(doChechLech)
