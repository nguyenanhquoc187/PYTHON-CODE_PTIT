def solve():
    s = input()
    s2 = ''
    for i in s:
        if i.isdigit(): s2+= i
        else: s2+=' '
    a = [ int(i) for i in s2.split() ]
    print(min(a))
for t in range( int(input())): solve()
a