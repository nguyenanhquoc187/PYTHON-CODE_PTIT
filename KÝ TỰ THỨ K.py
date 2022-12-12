def Try(f, n: int, k : int):
    if k == f[n]//2 + 1:
        return n
    elif k > f[n]//2 + 1:
        return Try(f,n-1,k - f[n-1] - 1)
    else: return Try(f,n-1,k)
t = int(input())
while t > 0:
    n, k = map(int,input().split())
    f = [0]*(n+1)
    f[1] = 1
    for i in range(2,n+1):
        f[i] = f[i-1]*2 + 1
    x = Try(f,n, k)
    print(format(ord('A') + x -1,'c'))
    t-=1