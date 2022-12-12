
class Matrix():
    a = []
    n, m = 0,0 
    def __init__(self, n, m, a):
        self.a = a
        self.n = n
        self.m = m
    def copy(self, b):
        self = b
    def chuyevi(self):
        b = []
        for i in range(m):
            c = []
            for j in range(n):
                c.append(a[j][i])
            b.append(c)
        self.a = b.copy()
    def tichmatran(self, b ):
        c = []
        for i in range(n):
            tmp = [0]*n
            c.append(tmp)
        for i in range(n):
            for j in range(n):
                tong = 0
                for k in range(m):
                    tong+= a[i][k]*b.a[k][j]
                c[i][j] = tong
        self.a = c.copy()
    def display(self):
        for i in range(n):
            for j in range(n):
                print(self.a[i][j], end = ' ')
            print()

for t in range(int(input())):
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    matran = Matrix(n,m,a)
    matran2 = Matrix()
    matran2.copy(matran)
    matran2.chuyevi()
    matran.tichmatran(matran2)
    matran.display()