def nguyento(n):
    if n == 0 or n == 1: return 0
    for i in range(2,int(n**0.5) +1):
        if n%i == 0: return False
    return True
def solve():
    n = input()
    a = [int(i) for i in input().split()]
    d = {}
    for i in a:
        if nguyento(i):
            if i in d: d[i]+=1
            else: d[i] = 1
    for i in d:
        print(i, d.get(i))
solve()