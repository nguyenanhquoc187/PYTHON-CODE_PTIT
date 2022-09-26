a = []
while len(a) < 10:
    a.extend(int(i) for i in input().split())
b = []
for i in a:
    b.append(i%42)
print(len(set(b))) 