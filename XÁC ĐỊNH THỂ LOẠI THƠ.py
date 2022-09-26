n = int(input())
check = 0
dem = 0
a = []
tmp = 0
for i in range(n):
    s = input().split()
    if len(s) == 6 and tmp != 8:
        dem+=1
        a.append(1)
    elif len(s) == 7 and tmp != 7:
        dem+=1
        a.append(2)
    if len(s) == 7:
        check+=1
    if check ==4: 
        tmp = 6
        check = 0
    else:tmp = len(s)
print(dem)
print(*a,sep = '\n')
