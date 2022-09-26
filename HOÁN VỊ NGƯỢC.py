import itertools
from math import factorial


for t in range(int(input())):
    n = int(input())
    print(factorial(n))
    a = list( itertools.permutations(range(1,n+1) ) )
    a.reverse()
    for i in a:
        for j in i:
            print(j, sep ='', end = '')
        print(end = ' ')
    print()