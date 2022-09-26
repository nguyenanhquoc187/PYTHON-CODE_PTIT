def solve():
    n = list(map(int,input()) )
    tong = 0; tich = 1
    x = len(n) -1 if (len(n) -1)% 2== 1 else len(n) - 2 
    for i in range(len(n)):
        if i%2== 1: tong+= n[i]
        elif n[i] != 0: tich *= n[i]
    print(tich, tong)
for t in range( int(input())): solve()
