s = input()
arr = []
for i in s:
    if i=="B":
        if not arr:
            continue
        arr.pop(-1)
    else:
        arr.append(i)
ans = ""
for i in arr:
    ans = "".join([ans,i])
print(ans)