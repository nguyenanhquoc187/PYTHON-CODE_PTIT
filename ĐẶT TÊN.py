
from itertools import combinations


n, k = map(int, input().split())
s = list(set(input().split() ) )
tohop = list(combinations(range(len(s)), k ))
s.sort()
ans = []
for i in tohop:
    res = ''
    for j in range(k):
        res = res  +  s[ i[j] ] + ' '
    ans.append(res)
ans.sort()
print(*ans, sep = '\n')