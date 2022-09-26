for t in range(int(input())):
    n,m = map(int,input().split())
    a = [int(i) for i in input().split()]
    Max = max(a)
    idx = a.index(Max)
    a.insert(idx,m)
    am = []
    duong = []
    for i in a:
        if i < 0: am.append(i)
        else: duong.append(i)
    am.extend(duong)
    print(*am, sep = ' ')