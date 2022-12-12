for t in range(int(input())):
    s = input()
    st = [0]
    soDauNgoacMo = 0
    for i in s:
        if i == '(':
            soDauNgoacMo+=1
            st.append(soDauNgoacMo)
            print(soDauNgoacMo, end = ' ')
        elif i == ')' :
            print(st.pop(), end = ' ')
    print()
