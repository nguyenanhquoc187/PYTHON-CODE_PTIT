for t in range(int(input() ) ):
    n = input()
    check = 1
    for i in n:
        if i != '4' and i != '7': check = 0 
    if check: print('YES')
    else: print('NO')