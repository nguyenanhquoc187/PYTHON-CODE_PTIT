d = {}
for t in range(int(input())):
    ma = input()
    ten = input()
    ht = input()
    d[ma] = ten + ' ' + ht
a = list(d.keys())
a.sort()
for i in a:
    print(i + ' ' + d.get(i))