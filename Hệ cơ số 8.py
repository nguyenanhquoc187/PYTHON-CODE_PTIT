def to10(s):
    s = list(s)
    s.reverse()
    n = 0
    for i in range(len(s)):
        if s[i] == '1': n+= 2**i 
    return n
def solve(): 
    s = input()
    n = to10(s)
    n = oct(n)
    print(n[2:])
solve()