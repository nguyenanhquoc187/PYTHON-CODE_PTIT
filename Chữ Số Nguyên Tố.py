def nguyento(n):
    if n == 0 or n == 1: return 0
    for i in range(2,int(n**0.5) +1):
        if n%i == 0: return 0
    return 1
def solve():
    n = input()
    dem = 0
    a = ['2' , '3' , '5' , '7']
    for i in n:
        if i in a: dem+=1
    if  nguyento(len(n)) and dem > len(n) -dem:
        print("YES")
    else: print("NO")
for t in range( int(input() ) ): solve()
