def solve():
    s = list(input())
    s.sort()
    res = 0
    while s[0].isnumeric():
        res += int(s[0])
        s.pop(0)
    print(*s,sep='',end = '')
    print(res)
for t in range(int(input())): solve()
        
