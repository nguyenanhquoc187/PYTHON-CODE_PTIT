def sangnguyento():
    isPrime = [1]*int(1e6)
    a = []
    for i in range(2,100000):
        if isPrime[i] == 1:
            a.append(i)
            for j in range(i*2,100000,i): 
                isPrime[j] = 0
    return a
a = sangnguyento()
n,x = map(int,input().split())
for i in range(n+1):
    print(x, end = ' ')
    x = x+a[i]
    