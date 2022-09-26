def Check_SoTangGiam(n):
    a = [int(i) for i in list(n)]
    x = 0 #vi tri tang giam
    for i in range(0, len(a)-1):
        if a[i]>a[i+1]:
            x = i
            break
        if a[i]==a[i+1]: return 0
    if x==len(a)-1 or x==0: return 0
    for i in range(x, len(a)-1):
        if a[i]<=a[i+1]: return 0

    return 1
def Check(n):
    if Check_SoTangGiam(n): print("YES")
    else: print("NO")

t = int (input())
while t>0:
    Check(input())
    t-=1