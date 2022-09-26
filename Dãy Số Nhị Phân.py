n = int(input())
a = [int(i) for i in input().split()]
count = 0
for i in range(len(a) - 1):
    if a[i] != a[i+1]: count+=1
print(count)