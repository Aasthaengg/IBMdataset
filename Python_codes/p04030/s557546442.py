S = input()
st = ''
for si in S:
    if si == '0':
        st += '0'
    if si == '1':
        st += '1'
    if si == 'B':
        if st == '':
            pass
        else:
            st = st[0:-1]
print(st)