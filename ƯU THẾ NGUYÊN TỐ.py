import math
def Check(n):
    if SNT(len(n))==0:
        return 0
    check = 0
    for i in n:
        if SNT(int(i)):
            check+=1
        else:
            check-=1
    if check>0:
        return 1
    return 0
def SNT(n):
    if n==2:
        return 1
    if n%2 ==0 or n<2:
        return 0
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i == 0:
            return 0
    return 1

t = int (input())
while t>0:
    n = input()
    if Check(n):
        print("YES")
    else:
        print("NO")
    t-=1