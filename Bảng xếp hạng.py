
n = int(input())
a = []
for i in range(n):
    s = input()
    c,t = [int(i) for i in input().split()]
    a.append( (s,c,t) )
a = sorted(a, key = lambda tmp: (-tmp[1],tmp[2], tmp[0] ))
for i in a:
    print(*i, sep = ' ')