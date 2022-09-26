
class Matrix():
    b = [ ]
    def __init__(self):
        self.matran =  [ ] 
    
    def chuyevi(self):
                


    def tichmatran(b):
        pass

for t in range(int(input())):
    n,m = map(int,input().split())
    a = Matrix()
    for i in range(n):
        b = list(map(int, input().split()))
        a.matran.append(b)

    # print(a.matran)
    a.chuyevi()
    
    for i in range(n):
        for j in range(n):
            print(a.matran[i][j], end = ' ')
        print()