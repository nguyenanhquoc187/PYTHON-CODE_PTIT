check = []
for i in range(0,1000000): check.append(1)
a = []
for i in range(2,1000000):
    if check[i] == 1: 
        a.append(i)
        for j in range(i*2, 1000000, i ): check[j] = 0
def solve():
    n = int(input())
    count = 0
    for i in a:
        if i >= n-6: break
        if check[i+6] == 1 and (check[i+2] == 1 or check[i+4] == 1):
            count+=1
    print(count)
for t in range(int(input())): solve()