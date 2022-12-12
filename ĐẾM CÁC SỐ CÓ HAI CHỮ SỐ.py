s = input()
if len(s)%2 ==0: n =len(s)
else: n = len(s) - 1
d = {}
for i in range(0,n,2):
    x = int(s[i] + s[i+1])
    if x not in d:
        d[x] = 1
    else: 
        d[x]+=1
for i in d.keys():
    print(i, d.get(i))