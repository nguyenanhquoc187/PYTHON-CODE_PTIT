def sangnguyento():
    global isPrime,prime
    for i in range(2,20000 +1):
        if isPrime[i]:
            prime.append(i)
            for j in range(i,20000 +1, i):
                isPrime[j] = 0
    
isPrime = [1]*(20001)
prime = []
sangnguyento()
n = int(input())
a = [2]
for i in range(1,len(prime)+1):
    if 2*2*prime[i]*prime[i] <= n:
        a.append(prime[i])
    else: break

dem = 0

for i in range(len(a) - 1):
    for j in range(i+1, len(a)):
        if a[i]*a[i]*a[j]*a[j] <=n:
            # print(a[i]*a[i]*a[j]*a[j])
            dem+=1
        else: break
for i in a[:7]:
    if i**8 <= n:
        dem+=1
print(dem)
    