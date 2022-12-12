def solve():
    s = input()
    ans = []
    if len(s) >= 100:
        for i in range(100):
            ans.append(s[i])
        if s[100] != ' ':
            while ans[len(ans) - 1] != ' ':
                ans.pop()
        print(''.join(ans))
    else: print(s)
for t in range(int(input())):
    solve()

    