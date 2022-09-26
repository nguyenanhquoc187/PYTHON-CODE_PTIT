import math
def Check(n):
    for i in range(0, len(n)):
        if (SNT(i) and SNT(int(n[i]))!=1) or (SNT(i)!=1 and SNT(int(n[i]))):
            return 0
    return 1

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