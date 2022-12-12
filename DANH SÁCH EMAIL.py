a = []
with open('CONTACT.in') as fileInput:
    for line in fileInput:
        a.append(line.strip().lower())
a = list(set(a))
a.sort()
print(*a, sep = '\n')