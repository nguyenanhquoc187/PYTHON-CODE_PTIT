def nguyento(n):
    if n == 0 or n == 1: return 0
    for i in range(2,int(n**0.5) +1):
        if n%i == 0: return False
    return True
n, m = map(int, input().split())
a = []
Max = 0
for i in range(n):
    b = [int(i) for i in input().split()]
    a.append(b)
for i in a:
    for j in i:
        if nguyento(j) and j > Max:
            Max = j
if Max == 0: print("NOT FOUND")
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == Max:
                print('Vi tri [' + str(i) + '][' + str(j) + ']'  )

