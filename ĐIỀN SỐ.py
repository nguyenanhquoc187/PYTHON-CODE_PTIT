def DienSo (a):
    n, L,R = len(a), min(a), max(a)
    res = 0
    for i in range(L,R+1):
        if i not in a: res+=1
    print(res)

t = int(input())
while t>0:
    n = int(input())
    a = sorted([int(i) for i in input().split()])
    DienSo (a)
    t-=1