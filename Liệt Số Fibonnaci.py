f = [0 ,1,1]
for i in range(3,93):
    f.append(f[i-1] + f[i-2])
def solve():
    a,b = [int(i) for i in input().split() ]
    for i in range(a,b+1):
        print(f[i], end =" ")
    print()
for t in range(int(input()) ): solve()