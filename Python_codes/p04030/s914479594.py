ans = []
for i in input():
    if i == "0":
        ans.append("0")
    elif i == "1":
        ans.append("1")
    else:
        if len(ans) == 0:
            None
        else:
            ans.pop()
print("".join(ans))