def nguyento(n):
    if n == 0 or n == 1: return 0
    for i in range(2,int(n**0.5) +1):
        if n%i == 0: return False
    return True
def main():
    n,m = [int(i) for i in input().split()]
    a = []
    for i in range(n):
        b = [int(j) for j in input().split() ]
        a.append(b)
    for i in range(n):
        for j in range(m):
            a[i][j] = 1 if nguyento(a[i][j]) else 0
    for i in a:
        print(*i, sep= ' ')
main()