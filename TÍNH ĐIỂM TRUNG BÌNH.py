n = int(input())
a = [float(i) for i in input().split()]
x = min(a)
while x in a: a.remove(x)
x = max(a)
while x in a: a.remove(x)
print('{:.2f}'.format(sum(a)/len(a) ) )