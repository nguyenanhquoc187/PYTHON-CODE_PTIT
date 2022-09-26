def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())
    a = set(a)
    print(len(a))
main()