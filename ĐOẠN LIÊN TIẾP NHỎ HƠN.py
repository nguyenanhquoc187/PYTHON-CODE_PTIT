t = int(input())
while t > 0:
    t -= 1
    n = int(input())
    s = list(map(int, input().split()))
    res = [1 for i in range(n)]
    stack = []
    for i in range(1, n):
        while len(stack) > 0 and s[i] >= s[stack[len(stack) - 1]]:
            res[i] += res[stack.pop()]
        stack.append(i)
    print(*res)