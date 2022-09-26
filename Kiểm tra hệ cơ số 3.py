def check(s: str):
    a = ['0' , '1', '2']
    for i in s:
        if i not in a: return False
    return True
def main():
    for t in range( int(input())):
        s = input()
        if check(s): print("YES")
        else: print("NO")
main()