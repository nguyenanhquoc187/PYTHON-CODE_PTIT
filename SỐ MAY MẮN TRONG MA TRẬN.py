from traceback import print_tb


n, m = map(int, input().split())
a = []
Max = 0; Min = int(1e9)
for i in range(n):
    b = [int(i) for i in input().split()]
    if max(b) > Max: Max = max(b)
    if min(b) < Min: Min = min(b)
    a.append(b)

luckyNumber = Max - Min
check = 0
for i in a:
    if luckyNumber in i: check = 1

if check == 0 : print("NOT FOUND")
else:
    print(luckyNumber)
    for i in range(n):
        for j in range(m):
            if a[i][j] == luckyNumber:
                print('Vi tri [' + str(i) + '][' + str(j) + ']'  )

