s = input()
ans = ""
for ss in s:
    if ss == "B":
        ans = ans[:-1]
    else:
        ans += ss
print(ans)