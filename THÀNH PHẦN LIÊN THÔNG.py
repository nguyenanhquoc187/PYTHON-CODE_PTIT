def DFS(u):
    global a,chuaxet
    chuaxet[u] = 0
    for i in a[u]:
        if chuaxet[i]: DFS(i)

n,m, x = map(int, input().split())
a = [[] for i in range(n+1) ]
for i in range(m):
    u,v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)
chuaxet = [1]*(n+1)
DFS(x)

for i in range(1,n+1):
    if chuaxet[i]:
        print(i)