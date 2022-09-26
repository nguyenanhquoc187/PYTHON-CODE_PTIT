

def countStep(strBase: str, strRoll: str):
    dem = 0
    while strRoll != strBase:
        dem+=1
        strRoll = list(strRoll)
        strRoll.append(strRoll.pop(0))
        strRoll = ''.join(strRoll)
        if dem > len(strRoll): return -1
    return dem

n = int(input())
a = []
for i in range(n): 
    a.append(input())

ok = 1
check = [0]*n
for i in range(n):
    for j in a:
        x = countStep(a[i], j )
        if x!= -1: check[i]+=x
        else: 
            ok = 0
            break
    if ok == 0: break
if ok!= 0 : print(min(check))
else: print(-1)
