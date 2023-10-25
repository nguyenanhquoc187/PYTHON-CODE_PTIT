import re

def cmp(o: str):
    a = o.split()
    a.reverse()
    a = ''.join(a)
    return a

d = {}
with open('SOTAY.txt') as fileinput:
    for line in fileinput:
        if re.match('^Ngay\s+\d{1,2}/\d{1,2}/\d{4}', line.strip()) != None:
            ngay = line.strip()[5:]
        elif re.match('\d', line.strip()) != None:
            sdt = line.strip()
            d[ten] = sdt, ngay
        else:
            ten = line.strip()
for i in sorted(d.keys(), key= cmp):
    print(i + ': ' + d[i][0] + ' ' + d[i][1])
        
        