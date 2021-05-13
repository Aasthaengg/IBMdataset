line = input()
ans = ""
for i in range(len(line)):
    if line[i] == "0" or line[i] == "1":
        ans += line[i]
    else:
        if ans != "":
            ans = ans[0:-1]
print(ans)