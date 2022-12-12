s = ''
daucau = ['.', '?', '!']
while 1:
    try:
        x = input()
        x = ' '.join(x.split())
        # if x == '1':
        #     break
        if x[-1] not in daucau:
            x+= '.'
        if x[-2] == ' ':
            x = list(x)
            x[-2] = ''
            x = ''.join(x)
        s+=  x
    except:
        break
a = ''
for i in s:
    a+= i
    if i in daucau:
        a = a.lower().capitalize()
        print(a)
        a = ''

