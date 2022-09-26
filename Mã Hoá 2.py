p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while 1:
    a = [str(i) for i in input().split()]
    if len(a) != 2: break
    k = int(a[0])
    s = a[1]
    k = int(k)
    if k ==0: break
    s = list(s)
    for i in range(len(s)):
        index = 0
        for j in range(len(p)):
            if p[j] == s[i]:
                index = j
                break
        
        s[i] = p[ (index+k)%28 ]
    s.reverse()
    s = "".join(s)
    print(s)