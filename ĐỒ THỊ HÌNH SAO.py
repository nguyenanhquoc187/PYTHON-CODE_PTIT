n = int(input())
a =[0]*(n+1)
for t in range(n-1):
    x,y = map(int,input().split())
    a[x]+=1
    a[y]+=1
def check():
    global n
    global a
    for i in a:
        if i == n-1:
            return "Yes"
    return "No"
print(check())
