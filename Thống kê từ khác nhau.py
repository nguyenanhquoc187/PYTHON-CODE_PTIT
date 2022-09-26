def xoadau(s: str):
    s = list(s)
    a = []
    for i in s:
        if i.isalnum() or i == ' ':
            a.append(i)
        else: a.append(' ')
    s = ''.join(a)
    return s
n = int(input())
ds = []
d = {}
for t in range(n):
    s = input()
    s = xoadau(s)
    a = s.split()
    for i in a:
        if i in d:
            d[i] += 1
        else: d[i] = 1
for i in d:
    ds.append( (i, d.get(i)) )
ds.sort( key = lambda k: (-k[1], k[0]) )
for i in ds:
    print(*i, sep = ' ')
    
