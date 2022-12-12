def nguyento(n):
    if n == 0 or n == 1: return 0
    for i in range(2,int(n**0.5) +1):
        if n%i == 0: return False
    return True

n = int(input())
a = [int(i) for i in input().split()]
d = {}
for i in a:
    d[i] = 1
b = list(d.keys())
m = len(b)
check = 0
for i in range(m):
    if nguyento(sum(b[0:i+1])) and nguyento(sum(b[i+1:m])):
        print(i)
        check = 1
        break
if check ==0: print('NOT FOUND')
