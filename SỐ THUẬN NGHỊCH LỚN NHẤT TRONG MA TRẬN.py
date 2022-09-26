def ktThuannghich(n: str):
    a = list(n)
    b = a.copy()
    b.reverse()
    return (a == b)

n, m = map(int, input().split())
a = []
for i in range(n):
    b = [int(i) for i in input().split()]
    a.append(b)
Max = 0
for i in a:
    for j in i:
        if j >= 10 and ktThuannghich(str(j)) and j > Max:
            Max = j
if Max == 0: print("NOT FOUND")
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == Max:
                print('Vi tri [' + str(i) + '][' + str(j) + ']'  )

