from collections import Counter
def to3(n: int):
    s = ''
    while n > 0:
        s+=str(n%3)
        n = n//3
    s = ''.join(list(reversed(s)))
    return s

a = []
j = 1
while len(a) < 1000:
    s3 = to3(j)
    c = Counter(s3)
    if c['2'] > len(s3)//2:
        a.append(s3)
    j+=1

t = int(input())
while t > 0:
    n = int(input())
    for i in range(n):
        print(a[i], end = ' ')
    print()
    t-=1