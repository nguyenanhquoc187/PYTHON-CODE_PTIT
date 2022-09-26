for t in range(int(input())):
    arr = [int(i) for i in input().split()]
    a = complex(arr[0],arr[1])
    b = complex(arr[2],arr[3])
    c = (a+b)*a
    d = (a+b)*(a+b)
    print("{:.0f} + {:.0f}i, {:.0f} + {:.0f}i".format(c.real,c.imag,d.real,d.imag))

