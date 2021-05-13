s = input()

st = []

for i in range(len(s)):
    if s[i] == "0":
        st.append("0")
    elif s[i] == "1":
        st.append("1")
    else:
        if len(st) != 0:
            st.pop()
        else:
            continue

print("".join(st))
