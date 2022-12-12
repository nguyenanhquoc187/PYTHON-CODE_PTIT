s = input()
k = int(input())
if len(s)%2 ==0: n =len(s)
else: n = len(s) - 1
d = {}
for i in range(0,n,2):
    x = int(s[i] + s[i+1])
    if x not in d:
        d[x] = 1
    else: 
        d[x]+=1
check = 0
for i in sorted(d.keys()):
    if d.get(i) >= k:
        check = 1
        print(i, d.get(i))
if check == 0: print('NOT FOUND')