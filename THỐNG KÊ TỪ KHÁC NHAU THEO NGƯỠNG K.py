def cmp(tmp):
    return (-int(tmp[1]),tmp[0])

n,k = map(int,input().split())
d = {}
kitu = [',', '.', '?', '!', ':', ';', '(',')', '-', '/']
for t in range(n):
    s = input().lower()
    s = list(s)
    for i in range(len(s)):
        if s[i] in kitu:
            s[i] = ' '
    s = ''.join(s)
    a = s.split()
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
a = sorted(d.items(),key = cmp)
for i in a:
    print(i[0],i[1])


    

