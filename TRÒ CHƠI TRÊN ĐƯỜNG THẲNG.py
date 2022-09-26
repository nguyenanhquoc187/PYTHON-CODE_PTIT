from math import gcd

# from người lạ with love
for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    Min = int(1e9)
    for i in range(n):
        for j in range(i+1,n):
            if gcd(a[i], a[j]) == 1:
                if c[i]  + c[j] < Min: Min = c[i] + c[j]
    if 1 in a and c[a.index(1)] < Min: Min = c[a.index(1)] 
    if Min == int(1e9):
        print(-1)
    else: print(Min)