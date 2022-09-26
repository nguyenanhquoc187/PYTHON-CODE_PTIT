def solve():
    n = input()
    a = [int(i) for i in input().split()]
    d = {}
    for i in a:
        if i in d: d[i]+=1
        else: d[i] = 1
    for i in d:
        if d.get(i) % 2  == 1:
            print(i)
            break
for t in range(int(input())): solve()