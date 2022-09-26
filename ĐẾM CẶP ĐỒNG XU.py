from math import factorial


def Ckn(n , k):
    return factorial(n)//(factorial(k)*factorial(n-k))
n = int(input())
a = []
for i in range(n):
    b = list(input())
    a.append(b)
soCapdongxu = 0
for i in a:
    dem = i.count('C')
    if dem >=2: soCapdongxu+= Ckn(dem,2)
for i in range(n):
    dem = 0
    for j in range(n):
        if a[j][i] == 'C': dem+=1
    if dem>=2: soCapdongxu+= Ckn(dem,2)
print(soCapdongxu)