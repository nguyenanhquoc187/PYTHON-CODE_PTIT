a1, a2 = [], []
with open('DATA1.in') as data1:
    for line in data1:
        line = line.lower()
        a1+= line.split()

with open('DATA2.in') as data1:
    for line in data1:
        line = line.lower()
        a2+= line.split()
a1 = set(a1)
a2 = set(a2)
b1 = a1 - a2
b2 = a2 - a1
b1 = sorted(list(b1))
b2 = sorted(list(b2))
print(*b1)
print(*b2)
    