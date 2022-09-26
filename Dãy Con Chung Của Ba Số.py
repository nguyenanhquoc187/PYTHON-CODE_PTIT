def solve():
    n,m,k = list(map(int, input().split() ) )
    a = list(map(int, input().split() ) )
    b = list(map(int, input().split() ) )
    c = list(map(int, input().split() ) )
    check,i,j,h = 0,0,0,0
    while i < n and j < m and h < k:
        if a[i]== b[j] == c[h]:
            check = 1
            print(a[i],end=' ')
            i,j,h = i +1, j+1, h+1
        elif a[i] < b[j]: i+=1
        elif b[j] < c[h]: j+=1
        else: h+=1
    if check == 0: print('NO', end ='')
    print()
for t in range(int(input())): solve()