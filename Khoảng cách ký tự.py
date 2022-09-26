def solve():
    s1 = list(input())
    s2 = list(reversed(s1)) 
    check = 1
    for i in range(1, len(s1) ):
        if abs(ord(s1[i])  - ord(s1[i-1]) ) != abs(ord(s2[i]) - ord(s2[i-1]) ):  check = 0
    if check == 1:
        print("YES")
    else: print("NO")
for t in range( int( input() )): solve()
