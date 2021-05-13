S = input()
ans = []
for s in S:
    if s == "0" or s == "1":
        ans.append(s)
    if s == "B":
        if ans:
            ans.pop(-1)
print("".join(ans))