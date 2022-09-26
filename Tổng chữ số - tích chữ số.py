def solve():
    n = list(map(int,input()) )
    tong = 0; tich = 0
    x = len(n) -1 if (len(n) -1)% 2== 1 else len(n) - 2 
    for i in range(len(n)):
        if i%2== 0: tong+= n[i]
        else:
            if i == x and tich == 0 and n[i] == 0: tich = 0
            elif n[i] != 0 :
                if tich == 0: tich = n[i]
                else: tich*= n[i]

    print(tong, tich)
for t in range( int(input())): solve()
