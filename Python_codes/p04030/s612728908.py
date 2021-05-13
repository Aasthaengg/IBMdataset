s = list(input())
output = []
for i in range(len(s)):
    if s[i] == "0":
        output.append("0")
    elif s[i] == "1":
        output.append("1")
    else:
        if len(output) > 0:
            output.pop()
        else:
            pass
print("".join(output))