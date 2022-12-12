with open('DATA.in.txt') as fileinput:
    data = fileinput.read()
a = data.split()
b = []
for i in a:
    try:
        x = int(i)
        if (x > 10**9):
            b.append(i)
    except ValueError:
        b.append(i)
b.sort() 
print(*b, sep = ' ')
