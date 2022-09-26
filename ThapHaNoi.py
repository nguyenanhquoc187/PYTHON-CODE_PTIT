def thap_ha_noi(n,a,b,c):
    if n == 1: chuyen(a,c)
    else:
        thap_ha_noi(n-1,a,c,b)
        chuyen(a,c)
        thap_ha_noi(n-1,b,a,c)
def chuyen(a,b):
    print(a + " -> " + b)
n = int(input())
thap_ha_noi(n,'A','B','C')
