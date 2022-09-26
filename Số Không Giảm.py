for t in range(int(input())):
    s = input()
    check = 1
    for i in range(0, len(s)-1):
        if s[i] > s[i+1]: 
            check = 0
            break
    if check: print('YES')
    else: print('NO')