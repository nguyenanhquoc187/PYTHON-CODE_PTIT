while True:
    n = int(input())
    if n == 0: break
    a = []
    for i in range(n): a.append( int(input()))
    a = set(a)
    if len(a) == 1: print('BANG NHAU')
    else: print(min(a), max(a))
