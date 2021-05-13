strs = []
s = list(input())
for num in s:
    if num == "0":
        strs.append("0")
    elif num == "1":
        strs.append("1")
    elif num == "B" and strs:
        strs.pop(len(strs)-1)

print("".join(strs))