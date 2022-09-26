n = int(input())
a = []
while len(a) < n:
    a.extend([int(i) for i in input().split()])
Max = max(a)
check = [0]*201
for i in a:
    check[i]+=1
ok = 1
for i in range(1, Max+1):
    if check[i] != 1:
        print(i)
        ok = 0
if ok == 1: print('Excellent!')
