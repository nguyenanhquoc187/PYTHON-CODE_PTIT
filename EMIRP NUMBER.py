check = []
for i in range(0,1000000): check.append(1)
a = []
for i in range(2,1000000):
    if check[i] == 1: 
        a.append(i)
        for j in range(i*2, 1000000, i ): check[j] = 0

def daonguoc(n: int):
    n = list(str(n))
    return int(''.join(reversed(n)))

b = []
for i in a:
    x = daonguoc(i)
    if x < int(1e6) and check[x] == 1 and x != i: 
        b.append(i)
        b.append(x)
        check[i] = check[x] = 0
def solve():
    n = int(input())
    for i in range(0,len(b),2):
        if b[i+1] < n: print(b[i], b[i+1], end = ' ')
    print()
for t in range(int(input())): solve()