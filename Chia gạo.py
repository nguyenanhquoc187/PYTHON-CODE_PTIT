
def Try(a, i, unused, per):
    for j in range(9):
        if unused[j] ==1:
            per[i] = j
            unused[j] = 0
            if i == 8:
                display(a, per)
            else:
                Try(a,i+1,unused,per)
            unused[j] = 1

def display(a : list, per):
    global ans
    x = a[per[0]] + a[per[1]] + a[per[2]]
    y = a[per[3]] + a[per[4]] + a[per[5]]
    z = a[per[6]] + a[per[7]] + a[per[8]]
    if max([x,y,z]) - min([x,y,z]) < ans:
        ans = max([x,y,z]) - min([x,y,z])

if __name__ == "__main__":
    a = [int(i) for i in input().split()]
    unused = [1]*9
    per = [0]*9
    ans = 10**9
    Try(a,0,unused,per)
    print(ans)
