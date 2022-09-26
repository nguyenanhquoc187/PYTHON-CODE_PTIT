n = input() 
dem = 0
for i in range(len(n) - 1, 0, -1):
    dem+=1
    if dem % 3 == 0:
        n = n[:i] + ',' + n[i:]
print(n)