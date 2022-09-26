import itertools
def main():
    n, k = map(int, input().split())
    a = set(  int(i) for i in input().split() )
    a = sorted(list(a))
    b = list( itertools.combinations( range(0, len(a)), k) )
    for i in b:
        for j in i:
            print( a[ j ], end = ' ')
        print()
main()
    