S = input()
ans = []
for c in S:
    if c == "B":
        if ans:
            ans.pop()
    else:
        ans.append(c)
print("".join(ans))
