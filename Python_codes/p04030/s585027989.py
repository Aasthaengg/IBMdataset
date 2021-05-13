S = input()

res = []
for s in S:
    if s == "0":
        res.append("0")
    elif s == "1":
        res.append("1")
    else:
        if res:
            res.pop()

print("".join(res))