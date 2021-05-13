s = list(input())
texit = []
for i in s:
    if i == "0":
        texit.append("0")
    elif i == "1":
        texit.append("1")
    elif i == "B" and len(texit) != 0:
        texit = texit[:-1]
print("".join(texit))