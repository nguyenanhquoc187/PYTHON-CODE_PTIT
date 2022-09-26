for t in range(int(input())):
    a = input().split('.')
    check = 1
    for i in a:
        try:
            x = int(i)
            if x < 0 or x > 255:
                check = 0
        except:
            check = 0
    if len(a) != 4: check = 0
    if check == 1:
        print('YES')
    else: print('NO')