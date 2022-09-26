def solve():
    a = []
    while len(a) < 4:
        a.extend( [ str(i) for i in input().split()] )
    x1 = a[2] ; x2 = a[3]; p = a[0]; q = a[1]
    if p > q: p,q = q,p
    print(Min(x1,p,q) + Min(x2,p,q), Max(x1,p,q) + Max(x2,p,q))  
def Min(x1,p,q):
    x1 = list(x1)
    for i in range(len(x1)):
        if x1[i] == q: x1[i] = p
    x1 = "".join(x1)
    x1 = int(x1)
    return x1
def Max(x1,p,q):
    x1 = list(x1)
    for i in range(len(x1)):
        if x1[i] == p: x1[i] = q
    x1 = "".join(x1)
    x1 = int(x1)
    return x1
for t in range( int(input()) ):solve()