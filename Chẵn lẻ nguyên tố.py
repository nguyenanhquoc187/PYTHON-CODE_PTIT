def nguyento(n):
    if n == 0 or n == 1: return 0
    for i in range(2,int(n**0.5) +1):
        if n%i == 0: return False
    return True
def solve(): 
    n = input()
    a = list(map(int,n) )
    sum = 0
    check = 1
    for i in range(len(a)):
        if i%2 == 0 and a[i] % 2 != 0: check =0
        if i% 2 == 1 and a[i] % 2 != 1: check = 0
        sum += a[i]
    if  not nguyento(sum) :    check = 0
    if check == 1: print("YES")
    else: print("NO")
for t in range( int(input()) ): solve()