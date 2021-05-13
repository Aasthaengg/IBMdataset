import sys
st = str(input())

st = sorted(st)

for i in st:
    if st.count(i) % 2 != 0:
        print('No')
        sys.exit()
print('Yes')