n = int(input())
a = list(map(int,input().split()))
check = [0]*30001
ok = 0
for i in a:
    check[i] = 1
for i in range(1,n+1):
    if check[i] == 0:
        ok = 1
        print(i)
        break
if ok == 0: print(n+1)