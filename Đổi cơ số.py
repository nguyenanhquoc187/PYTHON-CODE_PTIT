def Doi_co_so(n,b): #thap phan sang cac co so khac (b)
    res = []
    while n>0:
        if n%b<10:
            res.append(n%b)
        else:
            res.append(chr(ord('A')+n%b-10))
        n = int (n/b)
    for i in list(reversed(res)):
        print(i, end="")
    print()

t = int (input())
while t>0:
    n, b = map(int,input().split())
    Doi_co_so(n,b)
    t-=1