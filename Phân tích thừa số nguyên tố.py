for t in range( int(input()) ):
    n = int(input())
    print('1 * ', end ='')
    for i in range(2, int ( n**0.5 ) +1):
        mu = 0
        while n %i == 0:
            mu+=1
            n//=i
        if mu!= 0: 
            print(i,"^",mu,sep ='',end='')
            if n != 1: print(' * ',end='')
    if n!= 1: print(n,'^',1,sep ='',end='')
    print()