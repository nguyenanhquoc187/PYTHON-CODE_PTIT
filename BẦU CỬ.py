n, m = map(int,input().split())
a = [int(i) for i in input().split()]
d = {}
for i in a:
    if d.get(i) == None:
        d[i] = 1
    else:
        d[i] = d[i] + 1
Max = max(d.values())
Max2 = 0
index = -1
for i in d:
    if d[i] != Max and d[i] > Max2:
        Max2 = d[i]
        index = i
if Max2 ==0:
    print("NONE")
else:
    print(index)

    
