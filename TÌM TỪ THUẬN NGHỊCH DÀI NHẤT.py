def isThuanNghich(s: str):
    s1 = list(s)
    s1.reverse()
    return s == ''.join(s1)
d = {}
a = []
with open('VANBAN.in') as f:
    for line in f:
        a += line.strip().split()
ans = 0
for i in a:
    if isThuanNghich(i):
        if i not in d:
            d[i] = 1
        else: d[i] +=1
        ans = max(ans, len(i))
for i in d.keys():
    if len(i) == ans:
        print(i ,d[i])