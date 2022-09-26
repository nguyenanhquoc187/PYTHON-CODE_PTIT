def to4(n):
    s = ''
    while n > 0:
        s+= str(n%4)
        n = n//4
    s = list(s)
    s.reverse()
    s = ''.join(s)
    return s 
def to10(s):
    s = list(s)
    s.reverse()
    n = 0
    for i in range(len(s)):
        if s[i] == '1': n+= 2**i 
    return n
def solve():
    b = input()
    n = input()
    if b == '2': print(n)
    else:
        n = to10(n)
        if b == '4': print(to4(n))
        elif b == '8':
            n = oct(n)
            print(n[2:])
        else: 
            n = hex(n)
            n =n.upper()
            print(n[2:])
for t in range(int(input())): solve()