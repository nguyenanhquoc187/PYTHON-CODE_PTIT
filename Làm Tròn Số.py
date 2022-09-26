def solve():
    s = [ int(i) for i in input() ]
    for i in range(len(s)-1,0,-1):
        if s[i]>= 5: 
            s[i-1]+=1
        s[i] = 0
    print(*s,sep ='')
for t in range( int(input()) ): solve()