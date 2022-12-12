d = {}
n = int(input())
check = 1
tmp = ''
for j in range(n):
    s = input()
    if check == 1:
        tmp = s
        d[tmp] = 0
        check = 0
    elif s != '': 
        d[tmp]+=1
    if s == '':
        check = 1
for i in d.keys():
    print(i + ': ' + str(d.get(i) ) )

