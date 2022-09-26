def nguyento(n):
    if n == 0 or n == 1: return 0
    for i in range(2,int(n**0.5) +1):
        if n%i == 0: return False
    return True

n = input()
a = [int(i) for i in input().split()]
c = []
b = []
for i in range(len(a)):
    c.append(0)
    if nguyento(a[i]): 
        c[i] = 1
        b.append(a[i])
b.sort()
j = 0
for i in range(len(a)):
    if c[i] == 1:
        a[i] = b[j]
        j+=1
print(*a, sep = ' ')