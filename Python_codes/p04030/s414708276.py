s = input()
ans = []
for i in s:
    if i == "0" or i == "1":
        ans.append(i)
    elif ans != []:
        ans.pop(-1)
print("".join(ans))