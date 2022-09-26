def solve():
    n = input()
    a = [ int(i) for i in list(n) ]
    if check1(a) and check2(a):
        print("YES")
    else: print("NO")
def check1(a: list):
    sum = 0
    for i in a: sum+=i
    return (sum%10 == 0)
def check2(a: list):
    for i in range(1,len(a) -1):
        if abs(a[i+1] - a[i] ) != 2: return False
    return True
for t in range( int(input()) ): solve()