import math
n = int(input())
a = [int(i) for i in input().split()]
pay = 0
a.sort(reverse= True)
if n < 3:
    pay = sum( [(i-i//3) for i in a])
    print(pay)
else:
    i = 0
    while i <= n-3:
        x = a[i]+a[i+1]
        y = a[i] + a[i+1] + a[i+2]- (a[i]//3 + a[i+1]//3 + a[i+2]//3)
        pay += min(x,y)
        i+=3
    for j in range(n%3):
        pay += a[i+j] - a[i+j]//3
    print(pay)
