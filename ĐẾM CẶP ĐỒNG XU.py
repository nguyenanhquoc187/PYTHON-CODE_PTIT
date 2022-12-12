from math import comb

n = int(input())
a = []
for i in range(n):
    b = list(input())
    a.append(b)
soCapdongxu = 0
for i in a:
    dem = i.count('C')
    if dem >=2: soCapdongxu+= comb(dem,2)
for i in range(n):
    dem = 0
    for j in range(n):
        if a[j][i] == 'C': dem+=1
    if dem>=2: soCapdongxu+= comb(dem,2)
print(soCapdongxu)