a = []
for t in range(int(input())):
    s = list(input())
    for i in range(len(s)):
        if s[i].isalpha(): s[i] = ' '
    s = ''.join(s)
    a.extend( [int(i) for i in s.split() ] )
a.sort()
print(*a, sep = ' \n')