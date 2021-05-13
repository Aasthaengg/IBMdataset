line = input()
ans = ""
for i in range(len(line)):
    if line[i] == "0":
        ans += "0"
    elif line[i] == "1":
        ans += "1"
    else:
        if ans != "":
            ans = ans[0:-1]
print(ans)