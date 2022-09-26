for t in range(int(input())):
    n = int(input())
    used = [0]*1002
    for i in range(n):
        x = int(input())
        used[x]+=1
    Min = 1001
    for i in range(1,1001):
        if used[i] > used[Min]:
            Min = i
        elif used[i] == used[Min] and i < Min:
            Min = i
    print(Min)