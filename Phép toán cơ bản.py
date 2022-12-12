def kiemtra():
    global s,x
    s1 = s.copy()
    for i in x.keys():
        s1[i] = x[i]
    # print(s1)
    a = int(s1[0] + s1[1])
    b = int(s1[5] + s1[6] )
    c = 0
    if s1[3] == '+': c = a + b
    if s1[3] == '-': c = a - b
    if c < 10 or c > 99: return 0
    c = str(c)
    # print(c)
    if c[0] == s1[-2] and c[1] == s1[-1]: return c
    if s1[-2] == '?' and c[1] == s1[-1]: return c
    if c[0] == s1[-2] and s1[-1] == '?': return c
    if s1[-1] == '?' and s1[-2] ==  '?': return c
    return 0
    
def dequy(k ):
    global s,x,check
    pheptoan = ['+', '-']
    index = -1
    if s[k:7].count('?') != 0:
        index = s.index('?',k,7)
    if index == -1:
        c = kiemtra()
        if  c != 0:
            check = 1
            m = s.copy()
            for i in x.keys():
                m[i] = x[i]
            m[-2] = c[0];  m[-1] = c[1]
            print(''.join(m))
            return
    elif s[index] == '?' and index == 3:
        for j in pheptoan:
            x[index] = j
            dequy(index+1)
    elif s[index] == '?' and (index == 1 or index == 6):
        for j in range(10):
            x[index] = str(j)
            dequy(index+1)
    elif s[index] == '?' and (index == 0 or index == 5):
        for j in range(1,10):
            x[index] = str(j)
            dequy(index+1)
        
for t in range(int(input())):
    s = input()
    s = list(s)
    x = {}
    check = 0
    dequy(0)
    if check ==0 or s[5] in ['*', '/']:
        print('WRONG PROBLEM!')
        
    