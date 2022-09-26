def Xuly (s):
    res = []
    ktdb = ['.', '?', '!']
    s.lower()
    tmp = ""
    for i in s:
        if i in ktdb:
            res.append(tmp)
            tmp = ""
        else:
            tmp += i
            
    for i in res:
        i = " ".join(i.split())
        i = i.capitalize()
        print(i)
   
s = ""
while 1:
    try:
        s +=  input()
    except:
        break
Xuly(s)