

s = input()
hoa = 0 
for i in s:
    if i.isupper(): hoa+=1
if hoa > len(s) - hoa: print(s.upper())
else: print(s.lower())