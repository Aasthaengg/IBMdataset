s = list(input())
ans = []
for i in s:
    if i == "1":
        ans.append(1)
    elif i == "0":
        ans.append(0)
    else:
        if len(ans) == 0:
            continue
        else:
            del ans[-1]
for i in ans:
    print(i,end = "")