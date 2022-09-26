def dem(y):
    global x
    return abs(x - y)
n = int(input())
a = [int(i) for i in input().split()]
check = [0]*n
for i in range(n):
    x = a[i]
    check[i] = sum(map(dem,a))
indexMinNumber = check.index(min(check))
print(min(check) , a[indexMinNumber] )