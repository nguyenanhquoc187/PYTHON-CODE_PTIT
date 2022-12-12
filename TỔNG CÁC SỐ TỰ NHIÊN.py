def Try(n, tmp: list, k):
    if n == 0:
        global dem,a
        dem +=1
        a.append(tmp)
    else:
        for i in range(k,0,-1):
            if n - i >= 0:
                Try(n-i, tmp + [i] ,i)
        
for t in range(int(input())):
    n = int(input())
    dem = 0
    a = []
    Try(n,[],n)
    print(dem)
    for i in a:
        print(end = '(')
        s = ''
        for j in i:
            s+=str(j) + ' '
        print(s.strip(), end = ') ')
    print()
