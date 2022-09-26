def sangnguyento():
    global isPrime
    isPrime = [1]*int(1e6)
    isPrime[0] =isPrime[1] = 0
    for i in range(2,11111):
        if isPrime[i] == 1:
            for j in range(i*2,11111,i): 
                isPrime[j] = 0
    
def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    sangnguyento()
    minStep = 0
    for i in a:
        j = i
        k = i
        dem1= 0
        while isPrime[k] != 1:
            k-=1
            dem1+=1
        dem2= 0
        while isPrime[j] != 1:
            j+=1
            dem2+=1
        ans = min(dem1,dem2)
        minStep = max(minStep, ans)
    print(minStep)
            
main()