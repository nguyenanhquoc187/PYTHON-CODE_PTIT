def giaiHeptb2(a , b):
    '''
    x + y = a\n
    x - y = b
    '''
    return (a+b)//2, a- (a+b)//2

n = int(input())
a = [ [0] for i in range(n+1)]
for i in range(1, n+1):
    a[i].extend([int(i) for i in input().split()] )
if n == 2:
    print(1, a[1][2] - 1)
else:
    b = [0]*(n+1)
    for i in range(2,n):
        b[i], b[i+1] = giaiHeptb2(a[i][i+1], a[1][i] - a[1][i+1])
    b[1] = a[1][2] - b[2]
    print(*b[1:n+1])
