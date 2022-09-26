a, k, n = [int(i) for i in input().split() ]
check = 0
b = (a//k + 1)*k - a
if b <= n -a:
    for i in range(b,n-a+1,k):
        print(i,end =' ')
else: print(-1)
