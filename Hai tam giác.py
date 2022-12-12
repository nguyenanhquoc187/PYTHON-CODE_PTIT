# import itertools 

# def valid(a):
#     if (a[0] + a[1] > a[2] ) and (a[0] + a[2] > a[1]) and (a[1] + a[2] > a[0]):
#         return True
#     return False
# t = int(input())
# while t > 0:
#     a = [int(i) for i in input().split()]
#     hoanvi = list(itertools.permutations(a))
#     check = 0
#     for i in hoanvi:
#         if valid(i[0:3]) and valid(i[3:6]):
#             check = 1
#     print("yes" if check == 1 else "no")
#     t-=1

def Try(a, i, unused, per):
    for j in range(6):
        if unused[j] ==1:
            per[i] = j
            unused[j] = 0
            if i == 5:
                display(a, per)
            else:
                Try(a,i+1,unused,per)
            unused[j] = 1
def tontai(x,y,z):
    if (x + y > z ) and (x + z > y) and (y + z > x):
        return True
    return False
def display(a : list, per):
    global kiemtra
    x,y,z = a[per[0]], a[per[1]],a[per[2]]
    x2,y2,z2 = a[per[3]], a[per[4]], a[per[5]]
    if tontai(x,y,z) and tontai(x2,y2,z2):
        kiemtra =True
if __name__ == "__main__":
    for t in range(int(input())):
        a = [int(i) for i in input().split()]
        unused = [1]*6
        per = [0]*6
        kiemtra = False
        Try(a,0,unused,per)
        if kiemtra: print('yes')
        else: print('no')