import itertools
s = input()
per = itertools.permutations(list(s))
for i in list(per): print(''.join(i))