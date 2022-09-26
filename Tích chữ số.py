def solve(): 
    n = input()
    a = list( map(int,n) )
    sum = 1
    for i in a:
        if i != 0: sum*= i
    print(sum)
for t in range( int(input()) ): solve()
