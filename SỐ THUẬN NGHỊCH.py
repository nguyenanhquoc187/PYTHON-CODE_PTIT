def chuyen_co_so_K(n: int, k: int) -> str:
    s = ''
    while n > 0:
        s += str(n%k)
        n = n//k
    return s[::-1]
a,b,k = map(int, input().split())
dem = 0
for i in range(a,b+1):
    coSoK = chuyen_co_so_K(i, k)
    # print(coSoK)
    if coSoK == coSoK[::-1]:
        dem+=1
print(dem)