s = input()
op = ""
for i in range(len(s)):
    if s[i] == "0":
        op += "0"
    if s[i] == "1":
        op += "1"
    if s[i] == "B":
        op = op[:-1]
print(op)
