s = input()
ans = ""

for i in s:
    if i == "B":
        if not ans == "":
            ans = ans[:-1]
    else:
        ans = ans + i

print(ans)