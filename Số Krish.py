import math 
def solve():
    n = input()
    a = [int(i) for i in n ]
    sum = 0 
    for i in a:
        sum += math.factorial(i)
    if sum == int(n): 
        print("Yes")
    else: print("No")
for t in range( int(input()) ): solve()