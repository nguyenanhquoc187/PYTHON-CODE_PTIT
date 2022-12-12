s = input()
if len(s)%2 ==0: n =len(s)
else: n = len(s) - 1
a = []
for i in range(0,n,2):
    x = int(s[i] + s[i+1])
    if x not in a:
        a.append(x)
a.sort()
print(*a, sep = ' ')