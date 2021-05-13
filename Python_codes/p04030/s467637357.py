s = input()
n = len(s)

ans = []

for i in s:
    if i != "B":
        ans.append(i)
    else:
        if ans != []:
            ans.pop()
print("".join(ans))