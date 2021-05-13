s = list(input())
ans = []
for i in s:
    if i == "B":
        if ans == []:
            pass
        else:
            del ans[-1]
    else:
        ans.append(i)
print("".join(ans))